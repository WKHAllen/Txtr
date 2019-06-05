eel.expose(setTextColor);
function setTextColor(color) {
    document.documentElement.style.setProperty("--primary-color", color);
}

eel.expose(setBackgroundColor);
function setBackgroundColor(color) {
    document.documentElement.style.setProperty("--secondary-color", color);
}

eel.expose(setLogColor);
function setLogColor(color) {
    document.documentElement.style.setProperty("--log-color", color);
}

function onSubmit(event) {
    let input = document.getElementById("input");
    if (event.keyCode === 13) {
        let message = input.value;
        input.value = "";
        eel.sendMessage(message);
    } else if (event.keyCode === 27) {
        input.value = "";
    }
}

eel.expose(newMessage);
function newMessage(message, log) {
    log = log || log === undefined; // default to true
    let output = document.getElementById("output");
    let maxHeight = output.scrollHeight - output.clientHeight;
    let atBottom = false;
    if (output.scrollTop >= maxHeight) {
        atBottom = true;
    }
    let newmsg = document.createElement("p");
    newmsg.innerText = message;
    if(!log) {
        newmsg.classList.add("log");
    }
    output.appendChild(newmsg);
    if (atBottom) {
        output.scrollTop = output.scrollHeight;
    }
    if (log) {
        eel.logMessage(message);
    }
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

eel.expose(selectInput);
function selectInput() {
    let input = document.getElementById("input");
    input.focus();
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
