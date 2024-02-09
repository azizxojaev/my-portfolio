import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import uuid
from django.contrib.auth.models import User


def send_gmail(email, name, text):
    sender_address = 'shoprbexruzroot@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = sender_address
    message['Subject'] = f'Message from {name}'
    mail_content = f'Email: {email}\n Name: {name}\n\n{text}'
    message.attach(MIMEText(mail_content, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_address, "oshk bbyv tixg edwm")
    text = message.as_string()
    server.sendmail(sender_address, sender_address, text)
    server.quit() 
