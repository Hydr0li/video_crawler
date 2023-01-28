from flask import Flask
from .routes import main
import re
import os
import random
import string

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"
    
    app.register_blueprint(main)

    if not os.path.exists("downloads"):
        os.mkdir("downloads")

    return app


def createRandomString():
    randStr = ""
    strSet = string.digits + string.ascii_letters
    for i in range(10):
        randStr += random.choice(strSet)
    return randStr