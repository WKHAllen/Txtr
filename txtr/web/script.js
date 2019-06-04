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
    let maxHeight = output.scrollHeight - output.clientHeight;
    let atBottom = false;
    if (output.scrollTop >= maxHeight) {
        atBottom = true;
    }
    let newmsg = document.createElement("p");
    newmsg.innerText = message;
    output.appendChild(newmsg);
    if (atBottom) {
        output.scrollTop = output.scrollHeight;
    }
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
        output.style.height = `calc(100% - ${input.offsetHeight}px)`;
    } catch {
        let output = document.getElementById("output");
        output.style.height = "100%";
    }
    eel.onReady();
}

window.addEventListener("load", main);
