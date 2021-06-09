#!/usr/bin/python
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

def sendmail():
    while True:
        file = 'reports.xlsx'
        username='kanikasharma26597@gmail.com'
        password='ha10rs9h'
        send_from = 'kanikasharma26597@gmail.com'
        send_to = 'kanikasharma26597@gmail.com'
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime = True)
        msg['Subject'] = 'Attendance'
        server = smtplib.SMTP('smtp.gmail.com',587)
        port = '587'
        fp = open(file, 'rb')
        part = MIMEBase('application','vnd.ms-excel')
        part.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename='Attendance')
        msg.attach(part)
        smtp = smtplib.SMTP('smtp.gmail.com',587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(username,password)
        smtp.sendmail(send_from, send_to.split(','), msg.as_string())
        smtp.quit()
        break;
    return True
