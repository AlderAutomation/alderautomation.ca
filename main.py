from flask import Flask, render_template, request
import logging 

app = Flask(__name__)

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="./Logfiles/log.log", level=logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('/projects.html')


if __name__ == "__main__":
    app.run(debug=True)
