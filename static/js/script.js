function updateTime() {
    fetch('/current-zulu-time') // Assuming a backend endpoint
       .then(response => response.text())
       .then(data => {
            document.getElementById('time').innerHTML = 'Current Zulu Time: ' data;
        });
}

updateTime();
setInterval(updateTime, 60000); // Update every minute