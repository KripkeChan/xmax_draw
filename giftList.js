const giftGivers = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Diana", "Ethan"],
    "Charlie": ["Alice", "Diana"],
    "Diana": ["Bob", "Ethan"],
    "Ethan": ["Alice", "Charlie"]
};

function displayGiftList() {
    const user = localStorage.getItem('user');
    const peopleList = document.getElementById('peopleList');

    if (user && giftGivers[user]) {
        giftGivers[user].forEach(person => {
            const li = document.createElement('li');
            li.textContent = person;
            peopleList.appendChild(li);
        });
    } else {
        peopleList.innerHTML = "<li>No gift list found.</li>";
    }
}

function goBack() {
    localStorage.removeItem('user'); // Clear user from local storage
    window.location.href = 'index.html'; // Go back to the password page
}

// Call the function to display the gift list when the page loads
window.onload = displayGiftList;