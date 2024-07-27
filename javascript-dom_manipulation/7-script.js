document.addEventListener("DOMContentLoaded", function() {
    const listMovies = document.getElementById('list_movies');

    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Parse the JSON from the response
        })
        .then(data => {
            data.results.forEach(movie => {
                const listItem = document.createElement('li'); // Create a new <li> element
                listItem.textContent = movie.title; // Set the text content to the movie title
                listMovies.appendChild(listItem); // Append the <li> to the list
            });
        })
        .catch(error => {
            console.error('Error fetching movies:', error);
            const errorItem = document.createElement('li'); // Create a new <li> for the error message
            errorItem.textContent = 'Error fetching movie titles'; // Set error message
            listMovies.appendChild(errorItem); // Append the error message to the list
        });
});
