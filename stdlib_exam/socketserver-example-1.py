import socketserver
import time

# user-accessible port
PORT = 8037

# reference time
TIME1970 = 2208988800

class TimeRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print("connection from", self.client_address)
        t = int(time.time()) + TIME1970
        b = chr(t>>24&255) + chr(t>>16&255) + chr(t>>8&255) + chr(t&255)
        self.wfile.write(b)

server = socketserver.TCPServer(("", PORT), TimeRequestHandler)
print("listening on port", PORT)
server.serve_forever()

## connection from ('127.0.0.1', 1488)
## connection from ('127.0.0.1', 1489)
## ...
