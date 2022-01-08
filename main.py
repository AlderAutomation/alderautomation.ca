from flask import Flask, render_template, request
import logging 
import smtplib
from email.message import EmailMessage
import config

app = Flask(__name__)

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="./Logfiles/log.log", level=logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        send_email(name, email, subject, message)
        
    return render_template('index.html')


def send_email(name, email, subject, message):
    sendto = 'info@alderautomation.ca'
    user = config.user
    pwd = config.password
    content = 'Here is a new message from ' + name + ' at ' + email + '\n\n' + message

    message = EmailMessage()
    message.set_content(content)

    message['Subject'] = subject
    message['From'] = email
    message['To'] = sendto


    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.send_message(message)
    except Exception:
        print("Error")
    finally:
        if server is not None:
            server.quit()

if __name__ == "__main__":
    app.run(debug=True)
