import socket
import termcolor


# Configure the Server's IP and PORT
PORT = 8080
IP = "192.168.1.45"
MAX_OPEN_REQUESTS = 50

# Counting the number of connections
number_con = 0

# create the socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the raw message from the client, if any
        # The server waits for the message to arrive
        msg = clientsocket.recv(2048)
        print("Message from client: ", end="")
        termcolor.cprint(msg.decode("utf-8"), 'green')

        # Write a response to the message
        message = "Message received from the Server"
        send_bytes = str.encode(message)

        # We must write bytes, not a string
        clientsocket.send(send_bytes)

        # -- Finish the connection
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
