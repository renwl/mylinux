# a truly minimal HTTP proxy

import socketserver
import http.server
import urllib.request, urllib.parse, urllib.error

PORT = 1234

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.copyfile(urllib.request.urlopen(self.path), self.wfile)

httpd = socketserver.ForkingTCPServer(('', PORT), Proxy)
print("serving at port", PORT)
httpd.serve_forever()
