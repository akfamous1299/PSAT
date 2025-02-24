// Constants
const UPDATE_INTERVAL = 30000; // 30 seconds
const CURRENT_PAGE_ELEMENT = 'time';

// Function to update the zulu time
function updateZuluTime(zuluTime) {
    document.getElementById(CURRENT_PAGE_ELEMENT).innerHTML = zuluTime;
}

// Function to update the METAR table
function updateMetarTable(stations) {
    if (!Array.isArray(stations)) {
        console.error('Invalid stations data');
        return;
    }
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
    if (!Array.isArray(pireps)) {
        console.error('Invalid pireps data');
        return;
    }
    const pirepTableBody = document.querySelector('.pirep-table tbody');
    pirepTableBody.innerHTML = '';
    pireps.forEach(pirep => {
        const row = `
            <tr>
                <td>${pirep['Location']}</td>
                <td>${pirep['Time']}</td>
                <td>${pirep['Type']}</td>
                <td>${pirep['PIREP Text']}</td>
            </tr>
        `;
        pirepTableBody.innerHTML += row;
    });
}

// Function to update the block container
function updateBlockContainer(areaData, area) {
    if (!areaData || typeof areaData !== 'object') {
        console.error('Invalid area data');
        return;
    }
    const blockContainer = document.querySelector('.area-blocks-container');
    blockContainer.innerHTML = '';

    // Create containers for split left and right
    const leftContainer = document.createElement('div');
    leftContainer.className = 'split left';
    leftContainer.innerHTML = `<h3>${area} Area (Left)</h3>`;

    const rightContainer = document.createElement('div');
    rightContainer.className = 'split right';
    rightContainer.innerHTML = `<h3>${area} Area (Right)</h3>`;

    const leftSectors = [5, 6, 4, 15, 16];
    const rightSectors = [3, 9, 13, 7, 8];

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
        } else if (rightSectors.includes(areaData[nasId].Sector)) {
            rightContainer.innerHTML += blockHtml;
        }
    }

    // Append split containers to the main block container
    blockContainer.appendChild(leftContainer);
    blockContainer.appendChild(rightContainer);
    //console.log("updated blocks")
}

function showError(message) {
    const existingError = document.querySelector('.error-message');
    if (existingError) {
        existingError.remove();
    }
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    document.body.appendChild(errorDiv);
    setTimeout(() => errorDiv.remove(), 5000);
}

// Function to fetch updated data
function fetchUpdatedData(page) {
    if (!page) {
        console.error('Invalid page parameter');
        return;
    }
    // Add loading state
    document.body.classList.add('loading');

    fetch(`/fetch-updated-data/${page}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            updateZuluTime(data.zulu_time);
            if (page === "index") {
                // Update areas data
                for (let area in data.areas_data) {
                    if (area !== "HIGH") {
                        let tbody = document.getElementById(`stations-${area}`);
                        tbody.innerHTML = '';
                        for (let stationID in data.areas_data[area].pirep_status) {
                            let station = data.areas_data[area].pirep_status[stationID];
                            let latestPirepTime = station?.['Latest PIREP']?.['Time'] ?? 'None';
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
                updateBlockContainer(data.areas_data[area].pirep_status, area);
                //console.log("called for update with:", data.areas_data[area].pirep_status)
            } else {
                let area = page;
                // Update METAR and PIREP tables
                if (area !== "HIGH") {
                    updateMetarTable(data.areas_data[area].stations);
                }
                updatePirepTable(data.areas_data[area].pireps);
                console.log("called for update with:", data.areas_data[area].pireps)
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showError('Failed to fetch updated data. Please try again later.');
        })
        .finally(() => {
            document.body.classList.remove('loading');
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
    return currentUrl === '/' ? 'index' : currentUrl.slice(1);
}

// Initial data fetch
const currentPage = getCurrentPage();
fetchUpdatedData(currentPage);

// Update data every 30 seconds
setInterval(() => fetchUpdatedData(currentPage), UPDATE_INTERVAL);

// Add error handling for event listeners
window.addEventListener('load', () => {
    const logoElement = document.querySelector('.logo');
    const denaliButton = document.getElementById('denali-button');
    const closePopupButton = document.getElementById('close-popup');

    if (logoElement) {
        logoElement.addEventListener('click', () => {
            denaliButton?.click();
        });
    }

    if (denaliButton) {
        denaliButton.addEventListener('click', () => {
            const popup = document.getElementById('denali-popup');
            if (popup) popup.style.display = 'block';
        });
    }

    if (closePopupButton) {
        closePopupButton.addEventListener('click', () => {
            const popup = document.getElementById('denali-popup');
            if (popup) popup.style.display = 'none';
        });
    }
});
