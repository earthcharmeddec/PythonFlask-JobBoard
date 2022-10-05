import flask
from flask import Flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
