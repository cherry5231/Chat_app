const form = document.getElementById("messageForm");
const input = document.getElementById("messageInput");
const chatBox = document.getElementById("chatBox");

async function loadMessages() {

    const response = await fetch("/messages");

    const messages = await response.json();

    chatBox.innerHTML = "";

    messages.forEach(message => {

        const div = document.createElement("div");

        div.className = "message";

       div.innerHTML = `
    <div class="sender">
        ${message.username}
        <small>${message.time}</small>
    </div>

    <div class="text">
        ${message.text}
    </div>

    ${message.mine ? `
        <button onclick="deleteMessage(${message.id})">
            🗑 Delete
        </button>
    ` : ""}
`;

        chatBox.appendChild(div);

    });

    chatBox.scrollTop = chatBox.scrollHeight;
}

form.addEventListener("submit", async function(e){

    e.preventDefault();

    const formData = new FormData();

    formData.append("message", input.value);

    await fetch("/send",{

        method:"POST",

        body:formData

    });

    input.value="";

    loadMessages();

});
async function deleteMessage(id) {

    await fetch(`/delete/${id}`, {
        method: "POST"
    });

    loadMessages();
}
loadMessages();

setInterval(loadMessages,2000);
