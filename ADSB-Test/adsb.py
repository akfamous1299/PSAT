import requests
import geopy.distance
import time
import json


# Set up API credentials
#api_key = "YOUR_API_KEY"
api_url = "https://opensky-network.org/api/states/all"

# Set up list of airports
airports = [
    {"name": "ANC", "latitude": 61.186, "longitude": -149.998},
    {"name": "FAI", "latitude": 64.815, "longitude": -147.857}
]

# Set up distance threshold
threshold = 10  # miles

def get_aircraft_data():
    response = requests.get(api_url)
    data = response.json()
    return data["states"]

def calculate_distance(aircraft, airport):
    aircraft_lat = aircraft[6]
    aircraft_lon = aircraft[5]
    airport_lat = airport["latitude"]
    airport_lon = airport["longitude"]
    distance = geopy.distance.geodesic((aircraft_lat, aircraft_lon), (airport_lat, airport_lon)).miles
    return distance

def update_airports_with_nearby_planes():
    aircraft_data = get_aircraft_data()
    nearby_airports = []
    for aircraft in aircraft_data:
        for airport in airports:
            distance = calculate_distance(aircraft, airport)
            if distance <= threshold:
                nearby_airports.append(airport["name"])
    return nearby_airports

# Run the program
while True:
    nearby_airports = update_airports_with_nearby_planes()
    print("Airports with nearby planes:")
    for airport in nearby_airports:
        print(airport)
    print("\n")
    breakpoint()
    time.sleep(60)