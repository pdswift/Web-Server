#This script lunches a web sever and a restful interface
#CNA 335, winter 19
# Parker Swift, pdswift@student.rtc.edu
#base code from https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/
# !/usr/bin/env python


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
        message = "This web page runs on a pi and does a thing"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

 # starts a web server on port 5000
def run():
    print('starting server...')

    # Server setting
    server_address = ('172.25.107.95', 5000)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()
