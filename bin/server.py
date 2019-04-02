
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
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver,sys,json
from time import sleep


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        print("start")
        # sleep(10)
        length = self.headers.get('content-length')
        requestdata = self.rfile.read(int(length)).decode("utf-8")
        print(requestdata)
        requestdata = requestdata.replace("\'", "\"")
        requestobject = json.loads(requestdata)

        print(requestobject["command"])
        print(requestobject["parameter"]["leftwheel"])
        self._set_headers()
        print("stop")
        self.wfile.write(b"")

def run(server_class=HTTPServer, handler_class=S, port=50000):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
