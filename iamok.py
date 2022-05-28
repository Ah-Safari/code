import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


print('Sending to tell I am Ok')
email_sender = 'raspiconfig3@gmail.com'
email_receiver = 'raspiconfig3@gmail.com'
subject = 'I am Ok'

msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_receiver 
msg['Subject']= subject
body = 'Hey, I am Ok'
msg.attach(MIMEText(body, 'plain'))


text = msg.as_string()
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(email_sender, 'twibtkxjitigmttm')
connection.sendmail(email_sender, email_receiver, text )
connection.quit()