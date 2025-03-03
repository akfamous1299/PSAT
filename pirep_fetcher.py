import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import xml.etree.ElementTree as ET
import pytz
import requests
from shapely.geometry import Point, Polygon
import config

# Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Changed from DEBUG to INFO
handler = RotatingFileHandler('pirep_fetcher.log', maxBytes=10000, backupCount=3)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))

logger.addHandler(handler)

def point_in_polygon(lat, lon, polygon):
    shapely_polygon = Polygon(polygon)
    point = Point(lat, lon)
    return shapely_polygon.contains(point)

def find_polygons(lat, lon, alt):
    found_poly = []

    if lon >= 0:
        lon = -360+lon
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

    for area_name, area_data in config.areas.items():
        for sector_number, sector_polygon in area_data["sectors"].items():
            if found_poly == sector_number:
                area = area_name
                break
            

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

def bad_line_handler(line):
    """
    Handle malformed CSV lines by attempting to extract useful data
    Returns a properly formatted list or None if the line cannot be processed
    """
    if not line or len(line) < 3:  # Basic validation
        return None
        
    try:
        # Extract the minimum required fields
        receipt_time = line[0]
        observation_time = line[1]
        aircraft_ref = line[8]
        latitude = line[9]
        longitude = line[10]
        altitude = line[11]
        raw_text = line[41]
        
        # Validate essential fields
        if not all([receipt_time, observation_time, latitude, longitude]):
            return None
            
        # Return the line with validated fields
        return [receipt_time, observation_time, aircraft_ref, 
                latitude, longitude, altitude, raw_text]
        
    except (IndexError, ValueError):
        print(f"Could not process line: {line}")
        return None

def fetch_pirep_data():
    """
    Fetch PIREP data from the specified URL and filter by defined sectors.
    
    :return: List of PIREPs with relevant information
    """
    url = config.get_pirep_url()
    pasy_url = config.pasy_url
    
    try:
        response = requests.get(url)
        response_pasy = requests.get(pasy_url)
        
        #logger.debug(f"Main PIREP API Status Code: {response.status_code}")
        #logger.debug(f"PASY API Status Code: {response_pasy.status_code}")
        
        if response.status_code != 200 or response_pasy.status_code != 200:
            logger.error("Failed to fetch PIREP data")
            return []

        root = ET.fromstring(response.text)
        root_pasy = ET.fromstring(response_pasy.text)
        
        #main_pirep_count = len(root.findall(".//AircraftReport"))
        #pasy_pirep_count = len(root_pasy.findall(".//AircraftReport"))
        #logger.debug(f"Main PIREP count: {main_pirep_count}")
        #logger.debug(f"PASY PIREP count: {pasy_pirep_count}")

        pireps = []
        for xml_root in [root, root_pasy]:
            for pirep in xml_root.findall(".//AircraftReport"):
                try:
                    # Extract basic data from XML
                    lat = float(pirep.find("latitude").text)
                    lon = float(pirep.find("longitude").text)
                    alt = int(float(pirep.find("altitude_ft_msl").text)) if pirep.find("altitude_ft_msl") is not None else 0
                    raw_text = pirep.find("raw_text").text
                    receipt_time = pirep.find("receipt_time").text
                    observation_time = pirep.find("observation_time").text
                    report_type = pirep.find("report_type").text if pirep.find("report_type") is not None else ""
                    aircraft_ref = pirep.find("aircraft_ref").text if pirep.find("aircraft_ref") is not None else ""
                    
                    # Extract additional info
                    apt = extract_apt(raw_text)
                    rmk = extract_rmk(raw_text)
                    loc = extract_loc(raw_text)

                    # Find sector
                    sector_number = find_polygons(lat, lon, alt)

                    if sector_number:
                        # Convert observation time to formatted time
                        dt = datetime.strptime(observation_time, "%Y-%m-%dT%H:%M:%SZ")
                        formatted_time = dt.strftime('%H:%M')

                        # Find corresponding area
                        area_name = None
                        for area, area_data in config.areas.items():
                            if sector_number in area_data["sectors"]:
                                area_name = area
                                break

                        if area_name:
                            pireps.append({
                                "Location": loc,
                                "Receipt Time": receipt_time,
                                "RPT_TIME": observation_time,
                                "Time": formatted_time,
                                "Type": report_type,
                                "ACFT": aircraft_ref,
                                "ALT": alt,
                                "PIREP Remarks": rmk,
                                "PIREP Text": raw_text,
                                "Area": area_name,
                                "APT": apt,
                                "Sector": sector_number
                            })

                except (ValueError, AttributeError) as e:
                    logger.error(f"Error processing PIREP: {e}")
                    continue

        return pireps

    except ET.ParseError as e:
        logger.error(f"Failed to parse XML: {e}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error in fetch_pirep_data: {e}", exc_info=True)
        return []