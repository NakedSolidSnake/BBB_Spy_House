import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

my_password = "password"
my_address = "email"

def alertMe(subject, body):
  try:
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = my_address
    msg['Reply-to'] = my_address
    msg['To'] = my_address 

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_address, my_password)
    server.sendmail(my_address, my_address, msg.as_string())
    server.quit()
  except valueError:
    print "it wasn't possible to send email\n check your internet connection"

def sendAttach(subject, body, fileName):
  try:
    img_data = open(fileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = my_address
    msg['Reply-to'] = my_address
    msg['To'] = my_address 

    msg_subject = MIMEText(subject)
    msg.attach(msg_subject)
    msg_body = MIMEText(body)
    msg.attach(msg_body)
    image = MIMEImage(img_data, name=os.path.basename(fileName))
    msg.attach(image)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_address, my_password)
    server.sendmail(my_address, my_address, msg.as_string())
    server.quit()
  except valueError:
    print "it wasn't possible to send email\n check your internet connection"

  
