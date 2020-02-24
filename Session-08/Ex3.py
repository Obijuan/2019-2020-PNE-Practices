# -- Clinet chat example
import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.124.179"

while True:
    # -- Ask the user for a message
    m = input("Message to send: ")

    # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send data
    s.send(str.encode(m))

    # Closing the socket
    s.close()
