from flask import Flask, redirect, render_template, request, send_file
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


if __name__ == "__main__":
    app.run(debug=True)
