#!/usr/bin/env python

PORT     = 8001
CERTFILE = '/home/dwayne/.ssl/server.pem'

import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile=CERTFILE, server_side=True)
httpd.serve_forever()