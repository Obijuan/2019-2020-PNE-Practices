import socket
import termcolor


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @staticmethod
    def ping():
        print("OK!")

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"

    def debug_talk(self, msg_to_server):
        msg_from_server = self.talk(msg_to_server)
        print("To Server: ", end="")
        termcolor.cprint(msg_to_server, "blue")
        print("From Server: ", end="")
        termcolor.cprint(msg_from_server, "green")

        return msg_from_server

    def talk(self, msg):
        """Sent the string (message) to the app running in the given IP and Port"""

        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response
