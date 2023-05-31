# Kitronik Pico W Networking MicroPython
 
This repo contains a Networking MicroPython library file for the [Raspberry Pi Pico W](https://kitronik.co.uk/5345).

To use the library you can save the `PicoWNetworking.py` file onto the Pico W so it can be imported.

Also in this repo are some examples of how to use the library in the `Example Code` folder.

# How to use the Networking library for Pico W
Below is a small section explaining how to use each function from the Pico W Networking library.

The Server:
- [Setup the Server](https://github.com/KitronikLtd/Kitronik-Pico-W-Networking-MicroPython#setup-the-server)
- [Waiting for the Server to Start Up](https://github.com/KitronikLtd/Kitronik-Pico-W-Networking-MicroPython#waiting-for-the-server-to-start-up)
- [Waiting for Connection on the Server](https://github.com/KitronikLtd/Kitronik-Pico-W-Networking-MicroPython#waiting-for-connection-on-the-server)
- [Sending a Request on the Server](https://github.com/KitronikLtd/Kitronik-Pico-W-Networking-MicroPython#sending-a-request-on-the-server)
- [Receiving a Request on the Server](https://github.com/KitronikLtd/Kitronik-Pico-W-Networking-MicroPython#receiving-a-request-on-the-server)
- [Disconnect the Server](https://github.com/KitronikLtd/Kitronik-Pico-W-Networking-MicroPython#disconnect-the-server)

The Client:
- [Setup the Client](https://github.com/KitronikLtd/Kitronik-Pico-W-Networking-MicroPython#setup-the-client)
- [Waiting for the Client to Start Up](https://github.com/KitronikLtd/Kitronik-Pico-W-Networking-MicroPython#waiting-for-the-client-to-start-up)
- [Waiting for Connection on the Client](https://github.com/KitronikLtd/Kitronik-Pico-W-Networking-MicroPython#waiting-for-connection-on-the-client)
- [Sending a Request on the Client](https://github.com/KitronikLtd/Kitronik-Pico-W-Networking-MicroPython#sending-a-request-on-the-client)
- [Receiving a Request on the Client](https://github.com/KitronikLtd/Kitronik-Pico-W-Networking-MicroPython#receiving-a-request-on-the-client)
- [Disconnect the Client](https://github.com/KitronikLtd/Kitronik-Pico-W-Networking-MicroPython#disconnect-the-client)
<br/>

## The Server
### Setup the Server
To use the networking library for a Pico W server we first need to import the library and setup our server. To initialise our server we can use the `KitronikPicoWServer` class which will take an SSID and password as its inputs. Using the SSID and password it will setup an access point which other devices can connect to. We can store our SSID and password in the `secrects.py` file to separate this sensitive information from our code.
``` python
from PicoWNetworking import KitronikPicoWServer
from secrets import secrets
# Server - Start soft AP for client to connect to
server = KitronikPicoWServer(secrets["ssid"], secrets["password"])
```
<br/>

### Waiting for the Server to Start Up
Before we start accepting connections on the server, we want to make sure the server has finished starting up. To do this we'll repeatedly check in a loop whether the access point has is active and has connected. We'll do this using the `isAPConnected` function and loop continuously while it has not.
``` python
# While not turned on, waiting for access point
while not server.isAPConnected():
    pass
```
<br/>

### Waiting for Connection on the Server
With our server started up, we can now accept a connection from a client. To do this we'll use the `listenForClient` function inside of a try-except block. The rest of our server code should go inside of this try-except block as it will allow us to handle any errors from our network communication, without the program crashing. In the except block we want the server to disconnect and close the connection with a client if an error occurs.
``` python
try:
    # Listen for the client to open a communication channel
    server.listenForClient()
except:
    # Error occurred, close connection
    server.disconnect()
```
<br/>

### Sending a Request on the Server
Now our server has a client connected to it, they can start communicating with each other. The communication between them can go both ways. To communicate from the server to the client we can send them a message. To send the client a message we can use the `sendToClient` function which takes one input for our message to send, as a string.
``` python
message = ""
# Send message to client
server.sendToClient(message)
```
<br/>

### Receiving a Request on the Server
To receive a communication from the client to the server we can accept a message they have sent to us. To receive a message from the client we can use the `receiveFromClient` function which returns the message sent to us, as a string.
``` python
# Receive message from client
message = server.receiveFromClient()
```
<br/>

### Disconnect the Server
To disconnect the server we can use the `disconnect` function. This will close any connections it has with clients and disconnect the access point, meaning it will no longer be visible to connect to.
``` python
# Close connection
server.disconnect()
```
<br/>

## The Client
### Setup the Client
To use the networking library for a Pico W client we first need to import the library and setup our client. To initialise our client we can use the `KitronikPicoWClient` class which will take an SSID and password as its inputs. Using the SSID and password it will try to connect to an access point with that SSID using the password. We can store our SSID and password in the `secrects.py` file to separate this sensitive information from our code.
``` python
from PicoWNetworking import KitronikPicoWClient
from secrets import secrets
# Client - Connect to soft AP setup by the server
client = KitronikPicoWClient(secrets["ssid"], secrets["password"])
```
<br/>

### Waiting for the Client to Start Up
Before we try to create a communication channel to the server, we want to make sure we have connected to the server's access point. To do this we'll repeatedly check in a loop whether the client has connected to the access point. We'll do this using the `ifWifiConnected` function and loop continously while it has not connected.
``` python
# While not connected, waiting for connection
while not client.isWifiConnected():
    pass
```
<br/>

### Waiting for Connection on the Client
Now that our client is on the access point, we can create a direct connect to the server which we can communicate over. To do this we'll use the `connectToServer` function inside of a try-except block. The rest of our client code should go inside of this try-except block as it will allow us to handle any errors from our networking communication, without the program crashing. In the except block we want the client to disconnect and close the connection with the server if an error occurs.
``` python
try:
    # Connect to the server to open a communication channel
    client.connectToServer()
except:
    # Error occurred, close connection
    client.disconnect()
```
<br/>

### Sending a Request on the Client
Now our client has connected to the server, they can start communicating with each other. The communication between them can go both ways. To communicate from the client to the server we can send them a message. To send the server a message we can use the `sendToServer` function which takes one input for our message to send, as a string.
``` python
message = ""
# Send message to server
client.sendToServer(message)
```
<br/>

### Receiving a Request on the Client
To receive a communication from the server to the client we can accepts a message they have sent to us. To receive a message from the server we can use the `receiveFromServer` function which returns the message sent to us, as a string.
``` python
# Receive message from server
message = client.receiveFromServer()
```
<br/>

### Disconnect the Client
To disconnect the client we can use the `disconnect` function. This will close the connection it has with the server and disconnect from the access point, meaning it will no longer be able to communicate with the server.
``` python
# Close connection
client.disconnect()
```
<br/>