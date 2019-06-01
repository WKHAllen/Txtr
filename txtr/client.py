from dtplib import Client
import eel
import yaml
import os

CONFIGDEFAULTS = {
    'host': '127.0.0.1',
    'port': 35792,
    'textcolor': '#005fff',
    'backgroundcolor': '#1f1f1f',
    'password': None,
    'name': 'Anonymous'
}
CONFIGFILENAME = "client-config.yaml"
if os.path.exists(CONFIGFILENAME):
    with open(CONFIGFILENAME, "r") as f:
        CONFIG = yaml.load(f, Loader=yaml.FullLoader)
else:
    with open(CONFIGFILENAME, "w") as f:
        yaml.dump(CONFIGDEFAULTS, f)
    CONFIG = CONFIGDEFAULTS

def parseConfig():
    for key in CONFIGDEFAULTS.keys():
        if key not in CONFIG:
            CONFIG[key] = CONFIGDEFAULTS[key]

@eel.expose
def setColors():
    eel.setTextColor(CONFIG["textcolor"])
    eel.setBackgroundColor(CONFIG["backgroundcolor"])

@eel.expose
def sendMessage(message):
    data = {"name": CONFIG["name"], "message": message}
    client.send(data)

def onRecv(message, _):
    eel.newMessage(message)

def onDisconnected():
    eel.doAlert("Disconnected from server")

parseConfig()
client = Client(onRecv=onRecv, onDisconnected=onDisconnected)
client.connect(CONFIG["host"], CONFIG["port"])
client.send(CONFIG["name"])
eel.init("web")
eel.start("client.html", size=(800, 600))
client.disconnect()
