from dtplib import Client
import eel

def main():
    eel.init("web")
    eel.start("client.html", size=(800, 600))

if __name__ == "__main__":
    main()
