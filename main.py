from flask import Flask, render_template, request
import logging 
import smtplib, config

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
    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
 