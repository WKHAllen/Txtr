from dtplib import Client
import eel
import yaml
import os

CONFIGDEFAULTS = {
    'host': '127.0.0.1',
    'port': 35792,
    'textcolor': '#005fff',
    'backgroundcolor': '#1f1f1f'
}
CONFIGFILENAME = "client-config.yaml"
if os.path.exists(CONFIGFILENAME):
    with open(CONFIGFILENAME, "r") as f:
        CONFIG = yaml.load(f, Loader=yaml.FullLoader)
else:
    with open(CONFIGFILENAME, "w") as f:
        yaml.dump(CONFIGDEFAULTS, f)
    CONFIG = CONFIGDEFAULTS

@eel.expose
def setColors():
    if "textcolor" in CONFIG:
        eel.setTextColor(CONFIG["textcolor"])
    if "backgroundcolor" in CONFIG:
        eel.setBackgroundColor(CONFIG["backgroundcolor"])

def getAddr():
    if "host" in CONFIG:
        host = CONFIG["host"]
    else:
        host = CONFIGDEFAULTS["host"]
    if "port" in CONFIG:
        port = CONFIG["port"]
    else:
        port = CONFIGDEFAULTS["port"]
    return host, port

def main():
    addr = getAddr()
    eel.init("web")
    eel.start("client.html", size=(800, 600))

if __name__ == "__main__":
    main()
