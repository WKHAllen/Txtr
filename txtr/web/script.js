eel.expose(setTextColor);
function setTextColor(color) {
    document.getElementsByTagName("body")[0].style.color = color;
}

eel.expose(setBackgroundColor);
function setBackgroundColor(color) {
    document.getElementsByTagName("body")[0].style.backgroundColor = color;
}

function main() {
    eel.setColors();
}

window.addEventListener("load", main);
