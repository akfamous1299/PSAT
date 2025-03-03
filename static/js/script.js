// Constants
const UPDATE_INTERVAL = 5000; // 5 seconds
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
                <td>${pirep['APT']}</td>
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
    console.log('Updating block container via SSE');  // Debug log to confirm SSE updates
    const blockContainer = document.querySelector('.block-container');
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

// Remove the old interval-based update code
// Delete or comment out:
// - fetchUpdatedData function
// - setInterval call
// - Initial fetchUpdatedData call

// Modified SSE setup with reconnection logic
function setupEventSource() {
    let eventSource = null;

    function connect() {
        if (eventSource) {
            eventSource.close();
        }

        console.log('Setting up EventSource connection...');  // Debug log
        eventSource = new EventSource('/stream');

        eventSource.onmessage = function (event) {
            console.log('Received SSE message');  // Debug log
            try {
                const data = JSON.parse(event.data);

                if (data.reconnect) {
                    console.log('Server requested reconnection');
                    setTimeout(connect, 1000);
                    return;
                }

                if (data.error) {
                    console.error('Server error:', data.error);
                    showError('Server error occurred. Reconnecting...');
                    return;
                }

                // Update UI with data
                updateUI(data);
            } catch (error) {
                console.error('Error processing update:', error);
                showError('Error processing update');
            }
        };

        eventSource.onerror = function (error) {
            console.error('EventSource failed:', error);
            showError('Connection lost. Reconnecting...');
            eventSource.close();
            setTimeout(connect, 5000);
        };
    }

    // Initial connection
    connect();

    // Cleanup on page unload
    window.addEventListener('beforeunload', () => {
        if (eventSource) {
            eventSource.close();
        }
    });
}

// Add these new functions before the updateUI function
function updateBlockPage(areasData, currentPage) {
    try {
        const area = currentPage.split('-')[2];
        if (areasData[area] && areasData[area].pirep_status) {
            console.log(`Updating blocks for ${area}:`, areasData[area].pirep_status);
            updateBlockContainer(areasData[area].pirep_status, area);
        } else {
            console.error(`No data found for area: ${area}`);
        }
    } catch (error) {
        console.error('Error in updateBlockPage:', error);
    }
}

function updateAreaPage(areasData, currentPage) {
    try {
        if (areasData[currentPage]) {
            if (currentPage !== "HIGH") {
                updateMetarTable(areasData[currentPage].stations);
            }
            if (areasData[currentPage].pireps) {
                updatePirepTable(areasData[currentPage].pireps);
            }
        } else {
            console.error(`No data found for area: ${currentPage}`);
        }
    } catch (error) {
        console.error('Error in updateAreaPage:', error);
    }
}

// Separate UI update logic for better organization
function updateUI(data) {
    console.log('Received data:', data); // Debug log

    // Update the time regardless of page
    updateZuluTime(data.zulu_time);

    const currentPage = getCurrentPage();
    console.log('Current page:', currentPage); // Debug log

    try {
        if (currentPage === "index") {
            updateIndexPage(data.areas_data);
        } else if (currentPage.startsWith('area-block-')) {
            updateBlockPage(data.areas_data, currentPage);
        } else if (currentPage.startsWith('area/')) {
            // Fix for area pages
            const areaName = currentPage.split('/')[1];
            updateAreaPage(data.areas_data, areaName);
        } else {
            // Direct area pages
            updateAreaPage(data.areas_data, currentPage);
        }
    } catch (error) {
        console.error('Error in updateUI:', error);
        showError('Error updating page content');
    }
}

function updateIndexPage(areasData) {
    if (!areasData) {
        console.error('No areas data received');
        return;
    }

    for (let area in areasData) {
        if (area !== "HIGH") {
            let tbody = document.getElementById(`stations-${area}`);
            if (tbody) {
                let pireps = areasData[area].pirep_status;
                if (pireps) {
                    try {
                        const rows = Object.entries(pireps)
                            .map(([stationID, station]) => {
                                // Handle both possible PIREP time formats
                                const latestPirep = station['Latest PIREP'];
                                const pirepTime = latestPirep ?
                                    (latestPirep.Time || latestPirep['Time']) : 'None';

                                return `
                                    <tr>
                                        <td>${stationID}</td>
                                        <td>${pirepTime}</td>
                                        <td class="${getStatusClass(station.Status)}">${station.Status}</td>
                                    </tr>
                                `;
                            })
                            .join('');
                        tbody.innerHTML = rows;
                    } catch (error) {
                        console.error(`Error updating ${area} table:`, error);
                    }
                }
            }
        }
    }
}

// Add this helper function for status styling
function getStatusClass(status) {
    switch (status) {
        case 'Within 45 mins':
            return 'status-green';
        case 'Within 60 mins':
            return 'status-yellow';
        default:
            return 'status-red';
    }
}

// Initialize the SSE connection when the page loads
document.addEventListener('DOMContentLoaded', setupEventSource);

// Add debug logging to the getCurrentPage function
function getCurrentPage() {
    const currentUrl = window.location.pathname;
    console.log('Current URL:', currentUrl);  // Debug log

    // Remove trailing slash if present
    const cleanUrl = currentUrl.endsWith('/') ? currentUrl.slice(0, -1) : currentUrl;

    let page;
    if (cleanUrl === '' || cleanUrl === '/') {
        page = 'index';
    } else if (cleanUrl.startsWith('/area/')) {
        page = cleanUrl.slice(1); // Include 'area/' in the return
    } else if (cleanUrl.startsWith('/area-block/')) {
        page = 'area-block-' + cleanUrl.split('/').pop();
        console.log('Area block page detected:', page);  // Debug log
    } else {
        page = cleanUrl.slice(1);
    }

    console.log('Resolved page:', page);  // Debug log
    return page;
}

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
