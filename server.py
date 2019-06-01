from dtplib import Server
import eel

def main():
    eel.init("web")
    eel.start("server.html", size=(800, 600))

if __name__ == "__main__":
    main()
