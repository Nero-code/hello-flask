import json

import firebase_admin
from flask import Flask, render_template
from firebase_admin import credentials
from firebase_admin import db
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


with open(os.getenv("FIREBASE_KEYS"), 'r') as f:
    keys = json.load(f)

print(keys)
cred = credentials.Certificate(keys)
default_app = firebase_admin.initialize_app(cred, {
    "databaseURL": "https://hello-flask-896f8-default-rtdb.firebaseio.com/"
})


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/add/<name>')
def add_name(name):
    db.Reference.push(name)


@app.route('/delete')
def delete_name(name):
    db.reference().delete()
