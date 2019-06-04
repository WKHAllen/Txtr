eel.expose(setTextColor);
function setTextColor(color) {
    document.documentElement.style.setProperty("--primary-color", color);
}

eel.expose(setBackgroundColor);
function setBackgroundColor(color) {
    document.documentElement.style.setProperty("--secondary-color", color);
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
    try {
        let input = document.getElementById("input");
        let output = document.getElementById("output");
        output.style.marginBottom = `${input.offsetHeight}px`; // If I knew how to make this work with css I would do so
    } catch {}
    eel.onReady();
}

window.addEventListener("load", main);
