// Select the element with the id 'red_header'
const redHeaderElement = document.getElementById('red_header');

// Add a click event listener to the selected element
redHeaderElement.addEventListener('click', function() {
  // Select the header element
  const headerElement = document.querySelector('header');
  // Change the text color of the header to red
  headerElement.style.color = '#FF0000';
});
