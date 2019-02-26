#This script updates the zip code database
#CNA 335, winter 19
# Parker Swift, pdswift@student.rtc.edu
#base code from https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/
# !/usr/bin/env python

import mysql.connector
#connects to WAMP on localhost
conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='zip code data')
c = conn.cursor()

print('connected to zip_code_data database')
from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "This web page serches the zip code database"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

 # starts a web server on port 5000
def run():
    print('starting server...')

    # Server setting
    server_address = ('127.0.0.1', 5000)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

run()