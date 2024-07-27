document.addEventListener("DOMContentLoaded", function() {
    const characterDiv = document.getElementById('character');

    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Parse the JSON from the response
        })
        .then(data => {
            characterDiv.textContent = data.name; // Display the character name
        })
        .catch(error => {
            characterDiv.textContent = 'Error fetching character: ' + error.message; // Handle errors
        });
});
