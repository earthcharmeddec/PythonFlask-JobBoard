import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/jobs')
def jobs():
    return flask.render_template('index.html')
