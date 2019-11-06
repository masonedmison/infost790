import os
import psycopg2
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__, static_folder=os.path.abspath('static'))

# connect to db
conn = conn = psycopg2.connect(dbname=Config.dbname, user=Config.user, host=Config.host, password=Config.password)
# db cols 
cols = ['time1', 'date1', 'year1', 'month1', 'ald', 'nsp', 'police', 'tract', 'ward', 'zip', 'x', 'y', 'arson', 'assault', 'burglary', 'damage',
    'homicide', 'lv', 'robbery', 'sexoff']

# create cursor for duration of session 
cursor = conn.cursor()

app.config.from_object(Config)
bootstrap = Bootstrap(app)

from app import routes



