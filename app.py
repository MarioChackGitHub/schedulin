
# A very simple Flask Hello World app for you to get started with...
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import json
from flask import Flask

user = "MarioTheBridge"
passw = "thebridge1234"
host = "MarioTheBridge.mysql.pythonanywhere-services.com"
database = "MarioTheBridge$schedulin"

app = Flask(__name__)

db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
conn = db.connect()

@app.route('/')
def hello():
    return 'Hola gente de TheBridge!'

@app.route('/bye')
def bye():
    return "Adiós"

