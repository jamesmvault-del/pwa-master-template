#!/usr/bin/env python3
import http.server
import socketserver
import os
import socket

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '':
            self.path = '/index.html'
        return super().do_GET()
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

class ReuseAddrTCPServer(socketserver.TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        super().server_bind()

os.chdir('/home/runner/workspace')
with ReuseAddrTCPServer(("0.0.0.0", 5000), MyHTTPRequestHandler) as httpd:
    print("Serving on 0.0.0.0:5000")
    httpd.serve_forever()
