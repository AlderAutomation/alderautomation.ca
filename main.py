from crypt import methods
from flask import Flask, redirect, render_template, request, send_file
import logging 
import smtplib, config
from email.message import EmailMessage
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


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
    sendfrom = 'alderautomation@shaw.ca'
    sendto = 'info@alderautomation.ca'
    user = config.user
    pwd = config.password
    content = 'Here is a new message from ' + name + ' at ' + email + '\n\n' + message

    try:
        msg = MIMEMultipart()
        msg["From"] = sendfrom
        msg["To"] = sendto
        msg["Subject"] = subject
        msg.preamble = subject
        body = 'Here is a new message from ' + name + ' at ' + email + '\n\n' + message
        body = MIMEText(body) 
        msg.attach(body) 


        server = smtplib.SMTP("mail.shaw.ca", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, pwd)
        server.send_message(msg)
    except Exception as e:
        logger.exception(e)
        print("Error")
    finally:
        if server is not None:
            server.quit()


@app.route('/mheltmanresume')
def show_static_pdf():
    with open('./static/docs/MHeltmanResume.pdf', 'rb') as static_file:
        return redirect('../static/docs/MHeltmanResume.pdf')


@app.route('/calc_update')
def calc_update():
    return redirect("../static/updates/calc/test_update.zip")


@app.route('/calc_update/version')
def calc_update_version():
    return "0.01"


@app.route('/support')
def support_me():
    return render_template('support.html')


if __name__ == "__main__":
    app.run(debug=True)
