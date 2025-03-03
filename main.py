#main.py
from flask import Flask, render_template, Response, stream_with_context
import config  # Import the config file
from metar_fetcher import fetch_metar_data
from pirep_fetcher import fetch_pirep_data
from datetime import datetime, timedelta
import pytz
import logging
from logging.handlers import RotatingFileHandler
import json
import time
from cache_utils import FileCache
import threading

app = Flask(__name__)
app.json.sort_keys = False

# Setup logging
handler = RotatingFileHandler('psat.log', maxBytes=10000, backupCount=3)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)  # Changed from DEBUG to INFO

def get_area_data(stations: list, pireps: list, areas: list) -> dict:
    if not hasattr(config, 'priority_lists') or not hasattr(config, 'airport_data'):
        app.logger.error('Missing required config attributes')
        raise ValueError('Invalid configuration')
        
    areas_data = {}
    for area in areas:
        area_priority = config.priority_lists.get(area, [])
        area_stations = [ (airport, station) for station in stations for airport in config.airport_data if airport['ICAO ID'] == station['station_id'] and airport['Area'] == area ]
        area_stations.sort(key=lambda x: (area_priority.index(x[0]['NAS ID']) if x[0]['NAS ID'] in area_priority else len(area_priority), x[0]['NAS ID']))
        area_pireps = [pirep for pirep in pireps if pirep['Area'] == area]
        station_pirep_status = {}
        for station in area_stations:
            station_pireps = [pirep for pirep in area_pireps 
                            if pirep['APT'] == station[0]['NAS ID'] and 
                               (pirep['ALT'] <= station[1]['elevation'] + 10000 or 
                                'DURC' in pirep['PIREP Text'] or 
                                'DURD' in pirep['PIREP Text'])]
            
            # Sort by the full datetime string instead of just the time
            station_pireps.sort(
                key=lambda x: datetime.strptime(x['RPT_TIME'], "%Y-%m-%dT%H:%M:%SZ"),
                reverse=True
            )
            #print(station_pireps)
            
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
            'pireps': area_pireps,
            'pirep_status': station_pirep_status,
        }
    return areas_data

# Initialize cache with 30-second timeout
cache = FileCache(timeout=60)

# Add global lock for fetch operations
fetch_lock = threading.Lock()

def fetch_cached_data():
    global fetch_lock
    with fetch_lock:
        is_valid, cached_data = cache.get()
        if (is_valid):
            #app.logger.debug("Using cached data")
            return cached_data['stations'], cached_data['pireps']

        #app.logger.debug("Cache miss or expired, fetching fresh data from APIs...")
        try:
            stations = fetch_metar_data()
            pireps = fetch_pirep_data()
            cache.set({
                'stations': stations,
                'pireps': pireps,
                'timestamp': datetime.now(pytz.utc).isoformat()
            })
            #app.logger.debug("Cache updated with fresh data")
            return stations, pireps
        except Exception as e:
            app.logger.error(f"Error during data fetch: {e}")
            raise

# Add connection counter
active_connections = 0

@app.route('/stream')
def stream():
    def generate():
        global active_connections
        active_connections += 1
        
        try:
            while True:
                try:
                    now = datetime.now(pytz.utc)
                    stations, pireps = fetch_cached_data()
                    areas = ["NORTH", "SOUTH", "HIGH", "ATOP"]
                    areas_data = get_area_data(stations, pireps, areas)
                    zulu_time = now.strftime("%Y-%m-%d %H:%M Z")
                    
                    data = {
                        'zulu_time': zulu_time,
                        'areas_data': areas_data
                    }
                    
                    yield f"data: {json.dumps(data)}\n\n"
                    time.sleep(5)
                    
                except Exception as e:
                    app.logger.error(f'Stream error: {str(e)}')
                    yield f"data: {json.dumps({'error': str(e)})}\n\n"
                    time.sleep(5)
        finally:
            active_connections -= 1
    
    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no'  # Disable nginx buffering
        }
    )

@app.route('/')
def index():
    try:
        stations = fetch_metar_data()
        pireps = fetch_pirep_data()
        areas = ["NORTH", "SOUTH", "HIGH", "ATOP"]
        areas_data = get_area_data(stations, pireps, areas)
        now = datetime.now(pytz.utc)
        zulu_time = now.strftime("%Y-%m-%d %H:%M Z")
        #app.logger.info('Index page accessed successfully')
        return render_template('index.html', areas_data=areas_data, zulu_time=zulu_time)
    except Exception as e:
        app.logger.error(f'Error in index route: {str(e)}')
        return "An error occurred", 500

@app.route('/fetch-updated-data/<page>')
def fetch_updated_data(page):
    try:
        stations, pireps = fetch_cached_data()
        areas = ["NORTH", "SOUTH", "HIGH", "ATOP"]
        areas_data = get_area_data(stations, pireps, areas)
        now = datetime.now(pytz.utc)
        zulu_time = now.strftime("%Y-%m-%d %H:%M Z")
        app.logger.info(f'fetch-updated-data called for page: {page}')
        return {
            'zulu_time': zulu_time,
            'areas_data': areas_data
        }
    except Exception as e:
        app.logger.error(f'Error updating data: {str(e)}')
        return {"error": "Failed to fetch data"}, 500

@app.route('/area/<area_name>')
def area(area_name):
    try:
        if area_name not in ["NORTH", "SOUTH", "HIGH", "ATOP"]:
            return "Area not found", 404
        stations = fetch_metar_data()
        pireps = fetch_pirep_data()
        areas_data = get_area_data(stations, pireps, [area_name])
        now = datetime.now(pytz.utc)
        zulu_time = now.strftime("%Y-%m-%d %H:%M Z")
        return render_template('area.html', area_name=area_name, stations=areas_data[area_name]['stations'], pireps=areas_data[area_name]['pireps'], zulu_time=zulu_time)
    except Exception as e:
        app.logger.error(f'Error in area route: {str(e)}')
        return "An error occurred", 500

@app.route('/area-block/<area_name>')
def area_block(area_name):
    try:
        if area_name not in ["NORTH", "SOUTH", "HIGH", "ATOP"]:
            return "Area not found", 404
        stations = fetch_metar_data()
        pireps = fetch_pirep_data()
        areas_data = get_area_data(stations, pireps, [area_name])
        now = datetime.now(pytz.utc)
        zulu_time = now.strftime("%Y-%m-%d %H:%M Z")
        return render_template('area_block.html', area_name=area_name, area_data=areas_data[area_name], zulu_time=zulu_time)
    except Exception as e:
        app.logger.error(f'Error in area_block route: {str(e)}')
        return "An error occurred", 500

if __name__ == "__main__":
    app.logger.info('Application startup')
    app.run(threaded=True)  # Enable threading for multiple connections


