from http.server import BaseHTTPRequestHandler, HTTPServer
from gpiozero import LED

led=LED(18)

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global request
   # messagetosend = bytes('Take picture',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    request = self.requestline
    request = request[5 : int(len(request)-9)]
    print(request)
    
    if request=='Fall detected':
        led.on()
        
    
    return


server_address_httpd = ('192.168.43.44',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
httpd.serve_forever()