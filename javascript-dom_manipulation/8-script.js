document.addEventListener("DOMContentLoaded", function() {
    const helloDiv = document.getElementById('hello');

    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Parse the JSON from the response
        })
        .then(data => {
            helloDiv.textContent = data.hello; // Display the translated hello
        })
        .catch(error => {
            console.error('Error fetching hello:', error);
            helloDiv.textContent = 'Error fetching hello'; // Display error message
        });
});
