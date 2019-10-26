import os
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__, static_folder=os.path.abspath('static'))

app.config.from_object(Config)
bootstrap = Bootstrap(app)

from app import routes



