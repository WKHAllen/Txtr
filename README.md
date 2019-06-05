# Txtr

Txtr, or Texter, is a simple app that functions as a chat program. The program is written in Python, and makes use of [dtplib](https://github.com/WKHAllen/dtplib) and [eel](https://github.com/ChrisKnott/Eel).

## Intro

Currently, Txtr is not designed to do anything beyond sending chat messages, although the possibility of sending files is not far off. The project is not meant to compete with Skype, Discord, or any other popular text/voice chatting system. The purpose for it is purely educational.

## Configuration

Upon running the server/client binaries, a YAML configuration file will be created. By default, the `host` value in the server config file will be set to null. If this is the case, it is the equivalent of using `socket.gethostname()` in python, meaning that the server will be visible to the outside world. If this is not desirable, one might set the value to `127.0.0.1` instead.

The GUI is created by eel, which hosts a local webserver on port 8000 by default. The default `localport` option has been set to 8000 in server config and 8001 in client config. While changing this is not a problem, one should make sure two programs aren't trying to use the same port at the same time. What this means is **don't set the localport option to the same thing in server and client config files**.

The `port` option is the port that the actual server is hosted on. The default is port 35792.

The `password` value can technically be any object, not just strings. If it is set to null in server config, however, clients will be allowed to connect to the server, regardless of the password they send.

If `logfile` is not set to null, the server/client will log all messages that appear in the window to the log file. The log file is also loaded into the window upon startup.

Any config elements that have to do with color can be set to anything interpretable by CSS.

The other configuration options are fairly self-explanatory.
