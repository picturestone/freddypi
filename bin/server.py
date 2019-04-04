
#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import socketserver,sys,json
from configreader import ConfigReader
from time import sleep
from handler import Handler


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        length = self.headers.get('content-length')
        requestdata = self.rfile.read(int(length)).decode("utf-8").replace("\'", "\"")
        requestobject = json.loads(requestdata)
        handler = Handler()
        handler.handle(requestobject)
        self._set_headers()
        self.wfile.write(b"")

def run(server_class=ThreadingHTTPServer, handler_class=S):
    config = ConfigReader()
    ip = config.ip
    port = config.port
    server_address = (ip, int(port))
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    run()
