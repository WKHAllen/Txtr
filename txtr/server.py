from dtplib import Server
import eel
import yaml
import os
import time

configDefaults = {
    'host': None,
    'port': 35792,
    'textcolor': '#005fff',
    'backgroundcolor': '#1f1f1f',
    'password': None
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
def onReady():
    eel.setTextColor(config["textcolor"])
    eel.setBackgroundColor(config["backgroundcolor"])
    eel.newMessage("[{}] {} {}:{}".format(time.ctime(), "Server running on", *server.getAddr()))

def onRecv(conn, data, _):
    if conn in names:
        message = "<{}> {}".format(data["name"], data["message"])
    else:
        message = "{} joined".format(data)
        names[conn] = data
    eel.newMessage("[{}] {}".format(time.ctime(), message))
    server.send(message)

def onDisconnect(conn):
    message = "{} left".format(names[conn])
    eel.newMessage("[{}] {}".format(time.ctime(), message))
    server.send(message)

parseConfig()
options = {"port": 8000}
server = Server(onRecv=onRecv, onDisconnect=onDisconnect)
server.start(config["host"], config["port"])
eel.init("web")
eel.start("server.html", size=(800, 600), options=options)
server.stop()
