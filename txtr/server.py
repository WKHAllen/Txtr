from dtplib import Server
import eel
import yaml
import os
import time

CONFIGDEFAULTS = {
    'host': None,
    'port': 35792,
    'textcolor': '#005fff',
    'backgroundcolor': '#1f1f1f',
    'password': None
}
CONFIGFILENAME = "server-config.yaml"
if os.path.exists(CONFIGFILENAME):
    with open(CONFIGFILENAME, "r") as f:
        CONFIG = yaml.load(f, Loader=yaml.FullLoader)
else:
    with open(CONFIGFILENAME, "w") as f:
        yaml.dump(CONFIGDEFAULTS, f)
    CONFIG = CONFIGDEFAULTS
names = {}

def parseConfig():
    for key in CONFIGDEFAULTS.keys():
        if key not in CONFIG:
            CONFIG[key] = CONFIGDEFAULTS[key]

@eel.expose
def onReady():
    eel.setTextColor(CONFIG["textcolor"])
    eel.setBackgroundColor(CONFIG["backgroundcolor"])
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
server = Server(onRecv=onRecv, onDisconnect=onDisconnect)
server.start(CONFIG["host"], CONFIG["port"])
eel.init("web")
eel.start("server.html", size=(800, 600))
server.stop()
