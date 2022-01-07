import cgi
import smtplib
from email.message import EmailMessage

form = cgi.FieldStorage()
# name = form["name"].value
name = form.getvalue('name')
sender = form.getvalue('email')
subject = form.getvalue('subject')
formcontent = form.getvalue('message')

sendto = 'info@alderautomation.ca'
user = 'alderautomationsmtp@gmail.com'
pwd = 'r469JBdisk%'
content = 'Here is a new message from ' + name + ' at ' + sender + '\n' + formcontent

message = EmailMessage()
message.set_content(content)

message['Subject'] = subject
message['From'] = sender
message['To'] = sendto


try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.send_message(message)
except Exception as e:
    print("Error: ", + str(e))
finally:
    if server is not None:
        server.quit()

print(name)