from PicoWNetworking import KitronikPicoWServer
from secrets import secrets

# Server - Start soft AP for client to connect to
server = KitronikPicoWServer(secrets["ssid"], secrets["password"])

# While not turned on, waiting for access point
while not server.isAPConnected():
    pass

try:
    # Listen for the client to open a communication channel
    server.listenForClient()

    while True:
        message = "S"
        # Send message to client
        server.sendToClient(message)

        # Receive message from client
        message = server.receiveFromClient()
        print("Message from client:", message)

    # Close connection
    server.disconnect()
except:
    # Error occurred, close connection
    server.disconnect()
