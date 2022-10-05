import Flask
from Flask import render_template

app = Flask.Flask(__name__)


@app.route('/jobs')
def jobs():
    Flask.render_template('index.html')
