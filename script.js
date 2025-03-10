// frontend/script.js
document.getElementById("send-btn").addEventListener("click", function(){
    let inputBox = document.getElementById("user-input");
    let message = inputBox.value;
    if(message.trim() === ""){
        return;
    }
    addMessage("user", message);
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({message: message})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        addMessage("bot", data.response);
        inputBox.value = "";
    })
    .catch(error => {
        console.error("Error during fetch:", error);
        addMessage("bot", "Sorry, there was an error processing your request.");
    })
    .then(response => response.json())
    .then(data => {
        addMessage("bot", data.response);
        inputBox.value = "";
    });
});

function addMessage(sender, text) {
    let chatBox = document.getElementById("chat-box");
    let messageDiv = document.createElement("div");
    messageDiv.classList.add("chat-message");
    if(sender === "user") {
        messageDiv.classList.add("user-message");
    } else {
        messageDiv.classList.add("bot-message");
    }
    messageDiv.textContent = text;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}
