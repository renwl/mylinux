import http.server
import http.server

class Handler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ["/cgi"]

PORT = 8000

httpd = http.server.HTTPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
