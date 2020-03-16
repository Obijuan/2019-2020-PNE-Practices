import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Analize the request line
        req_line = self.requestline.split(' ')

        # Get the path. It always start with the / symbol
        path = req_line[1]

        # It contains the resource name without the / symbol
        # If this string is blank "", it means the main page
        path = path[1:]

        # -- Variable for sending the response back
        contents = ""

        # -- Status code
        status = 0

        # -- Content type header
        # -- Both, the error and the main page are in plain text in this examples
        content_type = 'text/plain'

        # -- Depending on the resource requested
        if path == "":
            termcolor.cprint("Main page requested", 'blue')

            # Message to send back to the clinet
            contents = "Welcome to my server"

            # Status code is ok
            status = 200
        else:
            # -- Resource NOT FOUND
            termcolor.cprint("ERROR: Not found", 'red')

            # Message to send back to the clinet
            contents = "Resource not available"

            # Status code is NOT FOUND
            status = 404

        # Generating the response message
        self.send_response(status)

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
