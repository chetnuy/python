#!/usr/bin/env python
# @author      : ash (nevernew@mail.ru)
# @created     : 16/11/2019
# @description : HTTP simple for share directory

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
