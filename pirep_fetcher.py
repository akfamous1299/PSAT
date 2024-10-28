import re
from datetime import datetime
from io import StringIO

import pandas as pd
import requests
from shapely.geometry import Point, Polygon

import config


def point_in_polygon(lat, lon, polygon):
    shapely_polygon = Polygon(polygon)
    point = Point(lat, lon)
    return shapely_polygon.contains(point)

def find_polygons(lat, lon, alt):
    found_poly = []

    if lon >= 0:
        lon = -180-(180-lon)
        #print(lon)

    point = Point(lat, lon)

    area = None

    for area_name, area_data in config.areas.items():
        for sector_number, sector_polygon in area_data["sectors"].items():
            #print(f"Testing {area_name},{sector_number}")
            poly = Polygon(sector_polygon)
            if poly.contains(point):
                found_poly.append(sector_number)
                #print(found_poly)
        

    if len(found_poly) > 1:
        if alt >= 29000:
            found_poly = max(found_poly)
        else:
            found_poly = min(found_poly)
    else:
        found_poly = found_poly[0]

    for area_name, area_data in config.areas.items():
        for sector_number, sector_polygon in area_data["sectors"].items():
            if found_poly == sector_number:
                area = area_name
                break

    #print(f"found in {found_poly} in {area}")
    return found_poly

def extract_apt(raw_text):
    match = raw_text.partition(" ")[0]
    if len(match) != 3 or not match.isalpha():
        for apt_data in config.airport_data:
            if match in apt_data["ICAO ID"]:
                match = apt_data["NAS ID"]
                break
    if match:
        return match
    return None

def extract_rmk(raw_text):
    match = raw_text.partition("/RM")[2]
    if match:
        return match
    return None

def extract_loc(raw_text):
    match = raw_text.partition(" U")[0]
    if match:
        return match
    return None


def format_time(iso_time):
    #Convert ISO 8601 time string to 'HH:MM' format.
    dt = datetime.fromisoformat(iso_time[:-1])  # Remove 'Z' for fromisoformat
    return dt.strftime('%H:%M')  # Format to 'HH:MM'

def fetch_pirep_data():
    """
    Fetch PIREP data from the specified URL and filter by defined sectors.

    :return: List of PIREPs with relevant information
    """
    url = config.get_pirep_url()
    #print(f"Fetching PIREP data from URL: {url}")  # Debugging
    response = requests.get(url)
    response_pasy = requests.get(config.pasy_url)

    if response.status_code != 200 or response_pasy.status_code != 200:
        print("Failed to fetch PIREP data.")
        return []

    # Read the CSV into a DataFrame, skip rows and handle headers appropriately
    try:
        df = pd.read_csv(StringIO(response.text), skiprows=5)
        df_pasy = pd.read_csv(StringIO(response_pasy.text), skiprows=5)
        #print(df_pasy)

        if not df.empty or not df_pasy.empty:
            df = pd.concat([df, df_pasy], ignore_index=True)
            #print(df)
        else:
            df = df
        #print(df)

    except ValueError as e:
        print(f"Failed to parse CSV: {e}")
        return []
    #print(f"DataFrame columns: {df.columns}")  # Debugging
    #print(f"DataFrame head:\n{df.head()}")  # Debugging

    pireps = []

    for _, row in df.iterrows():
        #print(f"Processing row: {row}")  # Debugging
        try:
            lat = float(row['latitude'])
            lon = float(row['longitude'])
            alt = int(row['altitude_ft_msl'])
            raw_text = row['raw_text']
            apt = extract_apt(raw_text)  # Extract the APT
            rmk = extract_rmk(raw_text)# Extract the RMK
            loc = extract_loc(raw_text)  # Extract the LOC
            #print(f"Extracted (lat: {lat}, lon: {lon})")  # Debugging

            sector_number = find_polygons(lat, lon, alt)

            formatted_observation_time = format_time(row['observation_time'])
            for area_name, area_data in config.areas.items():
                if sector_number in area_data["sectors"]:

                    pireps.append({
                            "Location": loc,
                            "Receipt Time": row['receipt_time'],
                            "RPT_TIME": row["observation_time"],
                            "Time": formatted_observation_time,
                            "Type": row['report_type'],
                            "ACFT": row['aircraft_ref'],
                            "ALT": alt,
                            "PIREP Remarks": rmk,
                            "WX String": row['wx_string'],
                            "PIREP Text": row['raw_text'],
                            "Area": area_name,
                            "APT": apt, 
                            "Sector": sector_number
                        })
                    #print(f"PIREP found in:{area_name}")
                    break

            #print(pireps)

        except ValueError as ve:
            print(f"Could not convert string to float: {ve}, row: {row}")  # Debugging
        except Exception as e:
            print(f"Unexpected error processing row: {e}")  # Debugging

    #print(f"Processed PIREPs: {pireps}")  # Debugging
    return pireps
