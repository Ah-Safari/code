import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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