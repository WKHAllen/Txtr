from dtplib import Client
import eel
import yaml
import os
import time
import sys

configDefaults = {
    'host': '127.0.0.1',
    'port': 35792,
    'localport': 8001,
    'textcolor': '#005fff',
    'backgroundcolor': '#1f1f1f',
    'logcolor': '#7f7f7f',
    'password': None,
    'showtimestamps': True,
    'logfile': None,
    'name': 'Anonymous'
}
configFilename = "client-config.yaml"
if os.path.exists(configFilename):
    with open(configFilename, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
else:
    with open(configFilename, "w") as f:
        yaml.dump(configDefaults, f)
    config = configDefaults

def parseConfig():
    for key in configDefaults.keys():
        if key not in config:
            config[key] = configDefaults[key]

@eel.expose
def logMessage(message):
    if config["logfile"] is not None:
        with open(config["logfile"], "a") as f:
            f.write(message + "\n")

def addTimestamp(message):
    if config["showtimestamps"]:
        message = "[{}] ".format(time.ctime()) + message
    return message

def loadLogfile():
    if config["logfile"] is not None:
        with open(config["logfile"], "r") as f:
            for line in f:
                eel.newMessage(line, False)

@eel.expose
def onReady():
    eel.setTextColor(config["textcolor"])
    eel.setBackgroundColor(config["backgroundcolor"])
    eel.setLogColor(config["logcolor"])
    loadLogfile()
    try:
        client.connect(config["host"], config["port"])
    except ConnectionRefusedError:
        eel.newMessage(addTimestamp("Unable to connect to {}:{}".format(config["host"], config["port"])))
    else:
        client.send({"name": config["name"], "password": config["password"]})
        eel.newMessage(addTimestamp("Connected to {}:{}".format(*client.getServerAddr())))
        eel.enableInput()

@eel.expose
def sendMessage(message):
    data = {"name": config["name"], "message": message}
    client.send(data)

def onRecv(message, _):
    eel.newMessage(addTimestamp(message))

def onDisconnected():
    eel.newMessage(addTimestamp("Disconnected from server"))
    eel.disableInput()

def onClose(*args, **kwargs):
    client.disconnect()
    logMessage(addTimestamp("Disconnected"))
    sys.exit()

parseConfig()
options = {"port": config["localport"]}
client = Client(onRecv=onRecv, onDisconnected=onDisconnected)
eel.init("web")
eel.start("client.html", size=(800, 600), options=options, callback=onClose)
