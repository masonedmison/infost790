import os
import psycopg2
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__, static_folder=os.path.abspath('static'))

# connect to db
conn = psycopg2.connect(dbname=Config.dbname, user=Config.user, host=Config.host, password=Config.password)

# create cursor for duration of session 
cursor = conn.cursor()

app.config.from_object(Config)
bootstrap = Bootstrap(app)

from app import routes



