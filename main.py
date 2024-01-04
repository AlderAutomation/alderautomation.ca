from flask import Flask, render_template, request
import smtplib, config
from email.message import EmailMessage
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import logging 

app = Flask(__name__)

LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename='./Logfiles/log.log', level=logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')


@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']

            logger.debug(f'{name} {email} {message}')
            send_email(name, email, message)

        return render_template('contact.html')


def send_email(name, email, message):
    sendfrom = 'alderautomation@shaw.ca'
    sendto = 'info@alderautomation.ca'
    user = config.user
    pwd = config.password

    try:
        msg = MIMEMultipart()
        msg["From"] = sendfrom
        msg["To"] = sendto
        msg.preamble = "Email from AlderAutomation website"
        body = 'Here is a new message from ' + name + ' at ' + email + '\n\n' + message
        body = MIMEText(body) 
        msg.attach(body) 


        server = smtplib.SMTP("mail.shaw.ca", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, pwd)
        server.send_message(msg)
        logger.debug(msg)
    except Exception as e:
        logger.exception(e)
        print("Error")
    finally:
        if server is not None:
            server.quit()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
 