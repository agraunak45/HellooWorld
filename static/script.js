// script.js

document.getElementById("signupForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var password = document.getElementById("password").value;
    var confirm_password = document.getElementById("confirm_password").value;

    if (password != confirm_password) {
        setMessage("Passwords do not match", "text-danger");
    } else {
        this.submit();
    }
});

function setMessage(message, className) {
    var messageDiv = document.getElementById("message");
    messageDiv.innerHTML = message;
    messageDiv.className = className;
    messageDiv.style.display = "block";
}
