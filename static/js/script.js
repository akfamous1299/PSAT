// Constants
const UPDATE_INTERVAL = 30000; // 30 seconds
const CURRENT_PAGE_ELEMENT = 'time';

// Function to update the zulu time
function updateZuluTime(zuluTime) {
    document.getElementById(CURRENT_PAGE_ELEMENT).innerHTML = zuluTime;
}

// Function to update the METAR table
function updateMetarTable(stations) {
    const metarTableBody = document.querySelector('.metar-table tbody');
    metarTableBody.innerHTML = '';
    stations.forEach(station => {
        const row = `
            <tr>
                <td>${station[0]['NAS ID']}</td>
                <td>${station[1]['visibility']}</td>
                <td>${station[1]['ceiling_altitude']}</td>
                <td>${station[1]['wx_string']}</td>
            </tr>
        `;
        metarTableBody.innerHTML += row;
    });
}

// Function to update the PIREP table
function updatePirepTable(pireps) {
    const pirepTableBody = document.querySelector('.pirep-table tbody');
    pirepTableBody.innerHTML = '';
    pireps.forEach(pirep => {
        const row = `
            <tr>
                <td>${pirep['Location']}</td>
                <td>${pirep['Time']}</td>
                <td>${pirep['Type']}</td>
                <td>${pirep['ALT']}</td>
                <td>${pirep['ACFT']}</td>
                <td>${pirep['PIREP Remarks']}</td>
            </tr>
        `;
        pirepTableBody.innerHTML += row;
    });
}

// Function to update the block container
function updateBlockContainer(areaData) {
    const blockContainer = document.querySelector('.area-blocks-container');
    blockContainer.innerHTML = '';

    // Create containers for split left and right
    const leftContainer = document.createElement('div');
    leftContainer.className = 'split left';
    leftContainer.innerHTML = '<h3>Left Area</h3>';

    const rightContainer = document.createElement('div');
    rightContainer.className = 'split right';
    rightContainer.innerHTML = '<h3>Right Area</h3>';

    const leftSectors = [5, 6, 4, 15, 16];
    const rightSectors = [3, 9, 13 ,7 , 8];

    for (const nasId in areaData) {
        const pirepStatus = areaData[nasId].Status;
        let blockClass = '';
        let title = '';
        //console.log(pirepStatus)

        // Determine block color and title based on status
        if (pirepStatus === 'Within 45 mins') {
            blockClass = 'green';
            title = pirepStatus;
        } else if (pirepStatus === 'Within 60 mins') {
            blockClass = 'yellow';
            title = pirepStatus;
        } else {
            blockClass = 'red';
            title = pirepStatus;
        }

        // Create the block element
        const blockHtml = `
            <div class="block ${blockClass}" title="${title}">
                <b>${nasId}</b>
            </div>
        `;

        // Append the block to the appropriate split container
        
        if (leftSectors.includes(areaData[nasId].Sector)) { // Example condition for Left or Right
            leftContainer.innerHTML += blockHtml;
        } else if(rightSectors.includes(areaData[nasId].Sector)) {
            rightContainer.innerHTML += blockHtml;
        }
    }

    // Append split containers to the main block container
    blockContainer.appendChild(leftContainer);
    blockContainer.appendChild(rightContainer);
    //console.log("updated blocks")
}


// Function to fetch updated data
function fetchUpdatedData(page) {
  fetch(`/fetch-updated-data/${page}`)
  .then(response => response.json())
  .then(data => {
          updateZuluTime(data.zulu_time);
          if (page === "index") {
              // Update areas data
              for (let area in data.areas_data) {
                  if (area!== "HIGH") {
                      let tbody = document.getElementById(`stations-${area}`);
                      tbody.innerHTML = '';
                      for (let stationID in data.areas_data[area].pirep_status) {
                          let station = data.areas_data[area].pirep_status[stationID];
                          let latestPirepTime = station?.['Latest PIREP']?.['Time']?? 'None';
                          let row = `
                              <tr>
                                  <td>${stationID}</td>
                                  <td>${latestPirepTime}</td>
                                  <td>${station.Status}</td>
                              </tr>
                          `;
                          tbody.innerHTML += row;
                      }
                  }
              }
          } else if (page.startsWith('area-block-')) {
              let area = page.split('-')[2];
              // Update block container
              updateBlockContainer(data.areas_data[area].pirep_status);
              //console.log("called for update with:", data.areas_data[area].pirep_status)
          } else {
              let area = page;
              // Update METAR and PIREP tables
              updateMetarTable(data.areas_data[area].stations);
              updatePirepTable(data.areas_data[area].pireps);
          }
      })
 .catch(error => {
          console.error('Error fetching updated data:', error);
          // Display error message to user or retry fetch operation
      });
}

// Function to get the current page
function getCurrentPage() {
    const currentUrl = window.location.pathname;
    if (currentUrl.startsWith('/area/')) {
        return currentUrl.split('/').pop();
    } else if (currentUrl.startsWith('/area-block/')) {
        return 'area-block-' + currentUrl.split('/').pop();
    }
    return currentUrl === '/'? 'index' : currentUrl.slice(1);
}

// Initial data fetch
const currentPage = getCurrentPage();
fetchUpdatedData(currentPage);

// Update data every 30 seconds
setInterval(() => fetchUpdatedData(currentPage), UPDATE_INTERVAL);