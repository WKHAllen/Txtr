eel.expose(setTextColor);
function setTextColor(color) {
    document.getElementsByTagName("body")[0].style.color = color;
    document.getElementById("input").style.border = "1px solid " + color;
}

eel.expose(setBackgroundColor);
function setBackgroundColor(color) {
    document.getElementsByTagName("body")[0].style.backgroundColor = color;
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
}

eel.expose(doAlert);
function doAlert(text) {
    alert(text);
}

function main() {
    eel.onReady();
}

window.addEventListener("load", main);
