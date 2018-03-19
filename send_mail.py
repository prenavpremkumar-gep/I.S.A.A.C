import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'enter your email_id'
password = 'enter your password'
sender = 'sender's email_id'
targets = ['recepient's email_id']

msg = MIMEText('Hi, how are you today?')
msg['Subject'] = 'Hello'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
print('Mail sent')
server.quit()