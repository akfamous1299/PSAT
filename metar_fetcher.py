# metar_fetcher.py
import numpy as np
import pandas as pd
import requests
from io import StringIO
from shapely import is_valid
from shapely.geometry import Point, Polygon

import config

def find_polygons(lat, lon, alt):
    found_poly = []

    if lon >= 0:
        lon = -180 - (180 - lon)
    point = Point(lat, lon)
    
    area = None
    for area_name, area_data in config.areas.items():
        for sector_number, sector_polygon in area_data["sectors"].items():
            poly = Polygon(sector_polygon)
            if poly.contains(point):
                found_poly.append(sector_number)

    if len(found_poly) > 1:
        if alt >= 29000:
            found_poly = max(found_poly)
        else:
            found_poly = min(found_poly)
    elif len(found_poly) == 1:
        found_poly = found_poly[0]
    else:
        return None

    return found_poly

def fetch_metar_data():
    url = "https://aviationweather.gov/api/data/dataserver?requestType=retrieve&dataSource=metars&stationString=%40AK&hoursBeforeNow=2&format=csv&mostRecent=false&mostRecentForEachStation=postfilter"
    response = requests.get(url)

    # Load the CSV data, skipping the first 5 rows to get to the header
    data = pd.read_csv(StringIO(response.text), skiprows=5)
    
    # Remove "SM" from the visibility column before converting to numeric
    data['visibility_statute_mi'] = data['visibility_statute_mi'].str.replace('+', '', regex=False)
    data['visibility_statute_mi'] = pd.to_numeric(data['visibility_statute_mi'], errors='coerce')

    # Check for BKN or OVC layers at or below 5000 ft
    def check_cloud_layers(row):
        cloud_layers = [
            (row['sky_cover'], row['cloud_base_ft_agl']),
            (row['sky_cover.1'], row['cloud_base_ft_agl.1']),
            (row['sky_cover.2'], row['cloud_base_ft_agl.2']),
            (row['sky_cover.3'], row['cloud_base_ft_agl.3']),
        ]
        lowest_ceiling = None
        for cover, base in cloud_layers:
            if cover in ['BKN', 'OVC'] and pd.notna(base) and base <= 5000:
                if lowest_ceiling is None or base < lowest_ceiling[1]:
                    lowest_ceiling = (cover, base)
        return lowest_ceiling

    # Check weather conditions
    weather_conditions = ["BLSN", "FZRA", "TS", "FZDZ", "GR", "FU", "VA", "PL", "FZFG"]

    def check_weather_conditions(row):
        if pd.notna(row['wx_string']):
            return any(condition in row['wx_string'] for condition in weather_conditions)
        return False

    filtered_stations = []
    for _, row in data.iterrows():
        visibility = row['visibility_statute_mi']
        lowest_ceiling = check_cloud_layers(row)
        weather_condition = check_weather_conditions(row)
        sector_number = find_polygons(row['latitude'], row['longitude'], 0)
        

        if pd.notna(visibility) and visibility <= 5 or lowest_ceiling or weather_condition:
            filtered_stations.append({
                'station_id': row['station_id'],
                'visibility': visibility if pd.notna(visibility) else "N/A",
                'ceiling_type': lowest_ceiling[0] if lowest_ceiling else "N/A",
                'ceiling_altitude': lowest_ceiling[1] if lowest_ceiling else "N/A",
                'wx_string': row['wx_string'] if pd.notna(row['wx_string']) else "N/A",
                'sector': sector_number
            })

    return filtered_stations
