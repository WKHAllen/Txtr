from dtplib import Server
import eel
import yaml
import os
import time
import sys

configDefaults = {
    'host': None,
    'port': 35792,
    'localport': 8000,
    'textcolor': '#005fff',
    'backgroundcolor': '#1f1f1f',
    'password': None,
    'showtimestamps': True,
    'logfile': 'server.log'
}
configFilename = "server-config.yaml"
if os.path.exists(configFilename):
    with open(configFilename, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
else:
    with open(configFilename, "w") as f:
        yaml.dump(configDefaults, f)
    config = configDefaults
names = {}

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

@eel.expose
def onReady():
    eel.setTextColor(config["textcolor"])
    eel.setBackgroundColor(config["backgroundcolor"])
    server.start(config["host"], config["port"])
    eel.newMessage(addTimestamp("Server running on {}:{}".format(*server.getAddr())))

def onRecv(conn, data, _):
    if conn in names:
        message = "<{}> {}".format(data["name"], data["message"])
    else:
        if config["password"] is None or config["password"] == data["password"]:
            message = "{} joined".format(data["name"])
            names[conn] = data["name"]
        else:
            server.removeClient(conn)
            return
    eel.newMessage(addTimestamp(message))
    server.send(message)

def onDisconnect(conn):
    message = "{} left".format(names[conn])
    eel.newMessage(addTimestamp(message))
    server.send(message)

def onClose(*args, **kwargs):
    server.stop()
    logMessage(addTimestamp("Server closed"))
    sys.exit()

parseConfig()
options = {"port": config["localport"]}
server = Server(onRecv=onRecv, onDisconnect=onDisconnect)
eel.init("web")
eel.start("server.html", size=(800, 600), options=options, callback=onClose)
