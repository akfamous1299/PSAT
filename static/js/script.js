function updateZuluTime() {
    // Get the current time in UTC
    const now = new Date();
    const hours = String(now.getUTCHours()).padStart(2, '0');
    const minutes = String(now.getUTCMinutes()).padStart(2, '0');

    // Format the Zulu time as "HH:MM Z"
    const formattedTime = `Current Zulu Time: ${hours}:${minutes} Z`;

    // Update the HTML content
    document.getElementById('time').innerHTML = formattedTime;
}

// Initial call to display the time immediately
updateZuluTime();

// Update every minute (60,000 milliseconds)
setInterval(updateZuluTime, 30000);

function fetchUpdatedData(page) {
    fetch(`/fetch-updated-data?page=${page}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('time').innerHTML = 'Current Zulu Time: ' + data.zulu_time;

            // Update station data for each area
            for (let area in data.areas_data) {
                let tbody = document.getElementById(`stations-${area}`);
                tbody.innerHTML = '';  // Clear existing data

                // Populate the table with updated data
                for (let stationID in data.areas_data[area].pirep_status) {
                    let station = data.areas_data[area].pirep_status[stationID];
                    let row = `<tr>
                        <td>${stationID}</td>
                        <td>${station.Latest_PIREP ? station.Latest_PIREP.Time : 'No PIREP Found'}</td>
                        <td>${station.Requirement}</td>
                    </tr>`;
                    tbody.innerHTML += row;
                }
            }
        })
        .catch(error => console.error('Error fetching updated data:', error));
}

// Function to determine the current page from the URL
function getCurrentPage() {
    return window.location.pathname.split("/").pop() || "index"; // Defaults to "index" if the last segment is empty
}

// Initial data fetch
const currentPage = getCurrentPage();
fetchUpdatedData(currentPage);  // Call with the current page name
setInterval(() => fetchUpdatedData(currentPage), 60000); // Refresh every minute



