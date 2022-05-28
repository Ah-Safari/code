from http.server import BaseHTTPRequestHandler, HTTPServer
from numbers import Number

Nbrequest= None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global Nbrequest
    Nbrequest=(Nbrequest if isinstance(Nbrequest,Number)else 0)+1
   # messagetosend = bytes((str('You got email')+str(Nbrequest)),"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    #self.send_header('Content-Length', len(messagetosend))
    self.end_headers() 
   # self.wfile.write(messagetosend)
    request = self.requestline
    request = request[5 : int(len(request)-9)]
    print(request)
    return
Nbrequest=0
server_address_httpd = ('192.168.43.44',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('starting server')
httpd.serve_forever()
    