#!/usr/bin/env python3
import http.server
import socketserver
import os

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '':
            self.path = '/index.html'
        return super().do_GET()

os.chdir('/home/runner/workspace')
with socketserver.TCPServer(("0.0.0.0", 5000), MyHTTPRequestHandler) as httpd:
    print("Serving on 0.0.0.0:5000")
    httpd.serve_forever()
