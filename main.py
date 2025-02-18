#main.py
from flask import Flask, render_template
import config  # Import the config file
from metar_fetcher import fetch_metar_data
from pirep_fetcher import fetch_pirep_data
from datetime import datetime
import pytz

app = Flask(__name__)
app.json.sort_keys = False

def get_area_data(stations, pireps, areas):
    areas_data = {}
    for area in areas:
        area_priority = config.priority_lists.get(area, [])
        area_stations = [ (airport, station) for station in stations for airport in config.airport_data if airport['ICAO ID'] == station['station_id'] and airport['Area'] == area ]
        area_stations.sort(key=lambda x: area_priority.index(x[0]['NAS ID']) if x[0]['NAS ID'] in area_priority else len(area_priority))
        area_pireps = [pirep for pirep in pireps if pirep['Area'] == area]
        station_pirep_status = {}
        for station in area_stations:
            station_pireps = [pirep for pirep in area_pireps if pirep['Location'] == station[0]['NAS ID']]
            station_pireps.sort(key=lambda x: x['Time'], reverse=True)
            if station_pireps:
                latest_pirep = station_pireps[0]
                now = datetime.now(pytz.utc)
                pirep_time = datetime.strptime(latest_pirep['RPT_TIME'], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.utc)
                time_diff = (now - pirep_time).total_seconds() / 60
            else:
                latest_pirep = None
                time_diff = None
            station_pirep_status[station[0]['NAS ID']] = {
                'Latest PIREP': latest_pirep,
                'Time Diff': time_diff,
                'Status': 'Within 45 mins' if time_diff is not None and time_diff <= 45 else 
                          'Within 60 mins' if time_diff is not None and time_diff <= 60 else 
                          'Over 60 mins' if time_diff is not None else 'No PIREP Found',
                'Sector': station[0]['Sector']
            }
        areas_data[area] = {
           'stations': area_stations,
            'pirep_status': station_pirep_status,
            'pireps': area_pireps
        }
    return areas_data

# Route to display METAR and PIREP data for each area
@app.route('/')
def index():
    stations = fetch_metar_data()
    pireps = fetch_pirep_data()
    areas = ["NORTH", "SOUTH", "HIGH", "ATOP"]
    areas_data = get_area_data(stations, pireps, areas)
    now = datetime.now(pytz.utc)
    zulu_time = now.strftime("%Y-%m-%d %H:%M Z")
    return render_template('index.html', areas_data=areas_data, zulu_time=zulu_time)

@app.route('/fetch-updated-data/<page>')
def fetch_updated_data(page):
    stations = fetch_metar_data()
    pireps = fetch_pirep_data()
    areas = ["NORTH", "SOUTH", "HIGH", "ATOP"]
    areas_data = get_area_data(stations, pireps, areas)
    now = datetime.now(pytz.utc)
    zulu_time = now.strftime("%Y-%m-%d %H:%M Z")
    return {
        'zulu_time': zulu_time,
        'areas_data': areas_data
    }

# Route to display data for a specific area
@app.route('/area/<area_name>')
def area(area_name):
    stations = fetch_metar_data()
    pireps = fetch_pirep_data()
    if area_name not in ["NORTH", "SOUTH", "HIGH", "ATOP"]:
        return "Area not found", 404
    areas_data = get_area_data(stations, pireps, [area_name])
    now = datetime.now(pytz.utc)
    zulu_time = now.strftime("%Y-%m-%d %H:%M Z")
    return render_template('area.html', area_name=area_name, stations=areas_data[area_name]['stations'], pireps=areas_data[area_name]['pireps'], zulu_time=zulu_time)

@app.route('/area-block/<area_name>')
def area_block(area_name):
    if area_name not in ["NORTH", "SOUTH", "HIGH", "ATOP"]:
        return "Area not found", 404
    stations = fetch_metar_data()
    pireps = fetch_pirep_data()
    areas_data = get_area_data(stations, pireps, [area_name])
    now = datetime.now(pytz.utc)
    zulu_time = now.strftime("%Y-%m-%d %H:%M Z")
    return render_template('area_block.html', area_name=area_name, area_data=areas_data[area_name], zulu_time=zulu_time)

if __name__ == "__main__":
    app.run()


