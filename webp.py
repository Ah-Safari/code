import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer
def turn(request):
    if request == 'On':
      GPIO.output(17,True)
    if request == 'Off':
      GPIO.output(17,False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
request = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global request
    messagetosend = bytes('Take picture',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    request = self.requestline
    request = request[5 : int(len(request)-9)]
    print(request)
    turn(request)
    '''if request == 'On':
      GPIO.output(17,True)
    if request == 'Off':
      GPIO.output(17,False)'''
    return


server_address_httpd = ('192.168.43.44',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
httpd.serve_forever()
GPIO.cleanup()

