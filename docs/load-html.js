function loadHTML(elementId, fileName) {
    fetch(fileName)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Could not load ${fileName}: ${response.statusText}`);
            }
            return response.text();
        })
        .then(data => {
            document.getElementById(elementId).innerHTML = data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
