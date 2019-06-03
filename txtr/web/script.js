eel.expose(setTextColor);
function setTextColor(color) {
    let body = document.getElementsByTagName("body")[0];
    body.style.color = color;
    try {
        let input = document.getElementById("input");
        input.style.border = "1px solid " + color;
    } catch {}
}

eel.expose(setBackgroundColor);
function setBackgroundColor(color) {
    let body = document.getElementsByTagName("body")[0];
    body.style.backgroundColor = color;
}

function onSubmit(event) {
    if (event.keyCode == 13) {
        let input = document.getElementById("input");
        let message = input.value;
        input.value = "";
        eel.sendMessage(message);
    }
}

eel.expose(newMessage);
function newMessage(message) {
    let output = document.getElementById("output");
    let newmsg = document.createElement("p");
    newmsg.innerText = message;
    output.appendChild(newmsg);
    eel.logMessage(message);
}

eel.expose(disableInput);
function disableInput() {
    let input = document.getElementById("input");
    input.setAttribute("disabled", "");
}

eel.expose(enableInput);
function enableInput() {
    let input = document.getElementById("input");
    input.removeAttribute("disabled");
}

function main() {
    eel.onReady();
}

window.addEventListener("load", main);
