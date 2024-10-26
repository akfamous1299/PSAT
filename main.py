from flask import Flask, render_template
import config  # Import the config file
from metar_fetcher import fetch_metar_data
from pirep_fetcher import fetch_pirep_data
from datetime import datetime
import pytz
import jsonify

app = Flask(__name__)

# Route to display METAR and PIREP data for each area
@app.route('/')
def index():
    # Fetch the METAR and PIREP data
    stations = fetch_metar_data()
    pireps = fetch_pirep_data()

    # Initialize the data structure for areas
    areas_data = {}

    # Define the areas to display (you can adjust as necessary)
    areas = ["NORTH", "SOUTH", "HIGH", "ATOP"]

    # Loop through each area and prepare the data
    for area in areas:
        # Get the priority list for the area from the config
        area_priority = config.priority_lists.get(area, [])
        area_stations = []

        # Filter the METAR stations based on the area's airport list
        for station in stations:
            for airport in config.airport_data:
                if airport['ICAO ID'] == station['station_id'] and airport['Area'] == area:
                    area_stations.append((airport, station))

        # Sort stations by priority (based on the NAS ID in the priority list)
        area_stations.sort(key=lambda x: area_priority.index(x[0]['NAS ID']) if x[0]['NAS ID'] in area_priority else len(area_priority))

        # Filter the PIREPs based on the area
        area_pireps = [pirep for pirep in pireps if pirep['Area'] == area]

        # Initialize a dictionary to store the PIREP requirement status for each station
        station_pirep_status = {}

        # Loop through each station to find the most recent PIREP and determine if a new one is required
        for station in area_stations:
            # Filter PIREPs for the current station
            station_pireps = [pirep for pirep in area_pireps if pirep['Location'] == station[0]['NAS ID']]
            
            # Sort PIREPs by time in descending order (newest first)
            station_pireps.sort(key=lambda x: x['Time'], reverse=True)
            

            # Check if there are any PIREPs for the station
            if station_pireps:
                # Get the most recent PIREP
                latest_pirep = station_pireps[0]

                # Calculate the time difference between now and the latest PIREP
                now = datetime.now(pytz.utc)
                pirep_time = datetime.strptime(latest_pirep['RPT_TIME'], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.utc)

                time_diff = (now - pirep_time).total_seconds() / 3600  # Convert to hours

                # Determine if a new PIREP is required (every hour)
                if time_diff >= 1:
                    station_pirep_status[station[0]['NAS ID']] = {'Latest PIREP': latest_pirep, 'Requirement': 'NEW PIREP REQUIRED'}
                else:
                    station_pirep_status[station[0]['NAS ID']] = {'Latest PIREP': latest_pirep, 'Requirement': 'Up to Date'}
            else:
                # If no PIREPs are found for the station, mark as 'NEW PIREP REQUIRED'
                station_pirep_status[station[0]['NAS ID']] = {'Latest PIREP': None, 'Requirement': 'NEW PIREP REQUIRED'}

        # Store both METAR and PIREP data in the dictionary
        areas_data[area] = {
            'stations': area_stations,
            'pirep_status': station_pirep_status
        }

    # Get Zulu time for the display
    now = datetime.now(pytz.utc)
    zulu_time = now.strftime("%Y-%m-%d %H:%M Z")

    # Render the index.html template with all the data
    return render_template('index.html', zulu_time=zulu_time, areas_data=areas_data)

@app.route('/fetch-updated-data')
def fetch_updated_data():
    # Call your existing functions to fetch METAR and PIREP data
    stations = fetch_metar_data()
    pireps = fetch_pirep_data()
    
    areas_data = {}  # Similar logic as in your index route to build areas_data

    # Build areas_data similar to the index function here...

    # Get Zulu time for the response
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

    # Ensure area_name exists in config
    if area_name not in ["NORTH", "SOUTH", "HIGH", "ATOP"]:
        return "Area not found", 404

    # Get priority list for the area
    area_priority = config.priority_lists.get(area_name, [])
    area_stations = []

    # Filter stations for the area
    for station in stations:
        for airport in config.airport_data:
            if airport['ICAO ID'] == station['station_id'] and airport['Area'] == area_name:
                area_stations.append((airport, station))

    # Sort stations based on the priority list
    area_stations.sort(key=lambda x: area_priority.index(x[0]['NAS ID']) if x[0]['NAS ID'] in area_priority else len(area_priority))

    # Filter PIREPs for the area
    area_pireps = [pirep for pirep in pireps if pirep['Area'] == area_name]

    # Get Zulu time
    now = datetime.now(pytz.utc)
    zulu_time = now.strftime("%Y-%m-%d %H:%M Z")

    # Render the area.html template with METAR and PIREP data
    return render_template('area.html', zulu_time=zulu_time, area_name=area_name, stations=area_stations, pireps=area_pireps)

if __name__ == "__main__":
    app.run(debug=True, port=5678)