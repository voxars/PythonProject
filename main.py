import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask import Flask,render_template

app = Flask(__name__)





@app.route("/")
def index():
    
    return render_template('index.html')