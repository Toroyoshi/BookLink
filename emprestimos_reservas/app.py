from flask import Flask
from controller import *

app = Flask(__name__)
# app.register_blueprint(user_blueprint, url_prefix='/users')