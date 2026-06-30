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

loadMessages();

setInterval(loadMessages,2000);