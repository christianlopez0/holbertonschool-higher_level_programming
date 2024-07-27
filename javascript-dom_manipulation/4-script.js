document.addEventListener("DOMContentLoaded", function() {
    const addItem = document.getElementById('add_item');
    const myList = document.querySelector('.my_list');

    addItem.addEventListener('click', function() {
        const newItem = document.createElement('li'); // Create a new <li> element
        newItem.textContent = 'Item'; // Set the text content of the new <li>
        myList.appendChild(newItem); // Append the new <li> to the list
    });
});
