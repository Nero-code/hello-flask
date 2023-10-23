import firebase_admin
from flask import Flask, render_template
from firebase_admin import credentials
from firebase_admin import db
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


cred = credentials.Certificate(os.getenv("FIREBASE_KEYS"))
default_app = firebase_admin.initialize_app(cred, {
    "databaseURL": "https://hello-flask-896f8-default-rtdb.firebaseio.com/"
})


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
