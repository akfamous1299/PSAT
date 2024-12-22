//script.js
/*function updateZuluTime() {
    // Get the current time in UTC
    const now = new Date();
    const month = String(now.getUTCMonth()+1).padStart(2, '0');
    const day = String(now.getUTCDate()).padStart(2, '0');
    const year = String(now.getUTCFullYear()).padStart(2, '0');
    const hours = String(now.getUTCHours()).padStart(2, '0');
    const minutes = String(now.getUTCMinutes()).padStart(2, '0');

    // Format the Zulu time as "HH:MM Z"
    const formattedTime = `Zulu Time: ${month}/${day}/${year} ${hours}:${minutes} Z`;

    // Update the HTML content
    document.getElementById('time').innerHTML = formattedTime;
}*/

// Update every minute (60,000 milliseconds)
function fetchUpdatedData(page) {
  fetch(`/fetch-updated-data/${page}`)
 .then(response => response.json())
 .then(data => {
    if (page === "index") {
      document.getElementById('time').innerHTML = data.zulu_time;
      for (let area in data.areas_data) {
        let tbody = document.getElementById(`stations-${area}`);
        tbody.innerHTML = '';  
        for (let stationID in data.areas_data[area].pirep_status) {
          let station = data.areas_data[area].pirep_status[stationID];
          let latestPirepTime = station?.['Latest PIREP']?.['Time']?? 'None';
          let row = `<tr>
              <td>${stationID}</td>
              <td>${latestPirepTime}</td>
              <td>${station.Requirement}</td>
            </tr>`;
          tbody.innerHTML += row;
        }
      }
    } else {
      document.getElementById('time').innerHTML = data.zulu_time;
      let metarTableBody = document.querySelector('.metar-table tbody');
      metarTableBody.innerHTML = '';  
      if (data.area_data && data.area_data.stations && Array.isArray(data.area_data.stations)) {
        for (let station of data.area_data.stations) {
          let row = `<tr>
              <td>${station[0]['NAS ID']}</td>
              <td>${station[1]['visibility']}</td>
              <td>${station[1]['ceiling_altitude']}</td>
              <td>${station[1]['wx_string']}</td>
            </tr>`;
          metarTableBody.innerHTML += row;
        }
      }
      let pirepTableBody = document.querySelector('.pirep-table tbody');
      pirepTableBody.innerHTML = '';  
      for (let pirep of data.area_data.pireps) {
        let row = `<tr>
            <td>${pirep['Location']}</td>
            <td>${pirep['Time']}</td>
            <td>${pirep['Type']}</td>
            <td>${pirep['ALT']}</td>
            <td>${pirep['ACFT']}</td>
            <td>${pirep['PIREP Remarks']}</td>
          </tr>`;
        pirepTableBody.innerHTML += row;
      }
    }
  })
 .catch(error => console.error('Error fetching updated data:', error));
}

function getCurrentPage() {
  const currentUrl = window.location.pathname;
  if (currentUrl.startsWith('/area/')) {
    return currentUrl.split('/').pop();
  }
  return currentUrl === '/'? 'index' : currentUrl.slice(1);
}

// Initial data fetch
const currentPage = getCurrentPage();
fetchUpdatedData(currentPage);  
setInterval(() => fetchUpdatedData(currentPage), 30000);