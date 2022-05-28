import smtplib


print('Sending to tell I am Ok')
server= smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("raspiconfig3@gmail.com","twibtkxjitigmttm")
server.sendmail("raspiconfig3@gmail.com","raspiconfig3@gmail.com","I am Ok")

server.quit()
'''
email_sender = 'raspiconfig3@gmail.com'
email_receiver = 'raspiconfig3@gmail.com'
subject = 'Photo from fall'
msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_receiver 
msg['Subject']= subject
body = 'Hey, I have fallen and I need help.'
msg.attach(MIMEText(body, 'plain'))
'''