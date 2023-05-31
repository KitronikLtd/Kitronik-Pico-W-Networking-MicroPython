from PicoWNetworking import KitronikPicoWClient
from secrets import secrets

# Client - Connect to soft AP setup by the server
client = KitronikPicoWClient(secrets["ssid"], secrets["password"])

# While not connected, waiting for connection
while not client.isWifiConnected():
    pass

try:
    # Connect to the server to open a communication channel
    client.connectToServer()

    # Receive message from server
    message = client.receiveFromServer()
    print("Message from server:", message)

    message = "Hello World, from client!"
    # Send message to server
    client.sendToServer(message)

    # Close connection
    client.disconnect()
except:
    # Error occurred, close connection
    client.disconnect()
