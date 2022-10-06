import flask
from flask import Flask,render_template, url_for

app = flask.Flask(__name__)


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')


url_for("jobs", filename= "../static/css/bulma.min.css")
url_for("jobs", filename2= "../static/css/app.css")
url_for("jobs", filename2= "https://use.fontawesome.com/releases/v5.2.0/css/all.css")
