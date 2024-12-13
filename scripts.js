const people = {
    "Alice": "!#2sd34",
    "Bob": "!#2@d44",
    "Charlie": "$#28k4",
    "Diana": "&2@d34",
    "Ethan": "@3%d34"
};

function submitPassword() {
    const passwordInput = document.getElementById('password').value;
    const user = Object.keys(people).find(person => people[person] === passwordInput);

    if (user) {
        localStorage.setItem('user', user); // Store the user in local storage
        window.location.href = 'giftList.html'; // Redirect to the gift list page
    } else {
        alert("Incorrect password! Please try again."); // Notification for incorrect password
    }
}