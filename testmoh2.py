import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer
import numpy as np
import cv2

import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

conf=False

def sendemail():
    print('Sending to make a photo')
    subprocess.call(['fswebcam', 'ImageToSend.jpg'])
    print('Image saved')
    print('Ready to send the email')
    email_sender = 'raspiconfig3@gmail.com'
    email_receiver = 'raspiconfig3@gmail.com'
    subject = 'Photo from fall'
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver 
    msg['Subject']= subject
    body = 'Hey, I have fallen and I need help.'
    msg.attach(MIMEText(body, 'plain'))

    #FILE PART
    filename = 'ImageToSend.jpg'
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet_stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= '+filename)
    msg.attach(part)
    #########

    text = msg.as_string()
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(email_sender, 'twibtkxjitigmttm')
    connection.sendmail(email_sender, email_receiver, text )
    connection.quit()
    print('Email sent')



def rescale_frame(frame,procent=75):
    #scale_procent=75
    width = int(frame.shape[1]*procent/100)
    height= int(frame.shape[0]*procent/100)
    dim=(width,height)
    return(cv2.resize(frame,dim,interpolation=cv2.INTER_AREA))


def turn(request):
    img_count=0
    if request == 'On':
      GPIO.output(17,True)
      while True:
            ret,frame=cap.read()
            if not ret:
                break
            frame = rescale_frame(frame,procent=100)
            cv2.imshow("capturing",frame)
            if  cv2.waitKey(33)== 27:
                break
            elif cv2.waitKey(33)==32:
                img_name="picture_{}.png".format(img_count)
                cv2.imwrite(img_name,frame)
                img_count+=1
                print("screeenshot taken")
    cap.release()
    cv2.destroyAllWindows()
      
    if request == 'Takepic':
        sendemail()
        conf=True
        


    if request == 'Ok':
        print("I am Ok")
      
      
cap=cv2.VideoCapture(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
request = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global request
    messagetosend=bytes('Nothing happend',"utf")
    if conf==True:
        messagetosend = bytes('Image Confirmed',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers() 
    self.wfile.write(messagetosend)
    request = self.requestline
    request = request[5 : int(len(request)-9)]
    print(request)
    turn(request)
    
    
    return


server_address_httpd = ('192.168.43.44',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
httpd.serve_forever()


