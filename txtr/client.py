from dtplib import Client
import eel
import yaml
import os
import sys

configDefaults = {
    'host': '127.0.0.1',
    'port': 35792,
    'localport': 8001,
    'textcolor': '#005fff',
    'backgroundcolor': '#1f1f1f',
    'password': None,
    'name': 'Anonymous'
}
configFilename = "client-config.yaml"
if os.path.exists(configFilename):
    with open(configFilename, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
else:
    with open(configFilename, "w") as f:
        yaml.dump(configDefaults, f)
    sys.exit() # config = configDefaults

def parseConfig():
    for key in configDefaults.keys():
        if key not in config:
            config[key] = configDefaults[key]

@eel.expose
def onReady():
    eel.setTextColor(config["textcolor"])
    eel.setBackgroundColor(config["backgroundcolor"])
    eel.newMessage("{} {}:{}".format("Connected to", *client.getServerAddr()))

@eel.expose
def sendMessage(message):
    data = {"name": config["name"], "message": message}
    client.send(data)

def onRecv(message, _):
    eel.newMessage(message)

def onDisconnected():
    eel.doAlert("Disconnected from server")

parseConfig()
options = {"port": 8001}
client = Client(onRecv=onRecv, onDisconnected=onDisconnected)
client.connect(config["host"], config["port"])
client.send(config["name"])
eel.init("web")
eel.start("client.html", size=(800, 600), options=options)
client.disconnect()
