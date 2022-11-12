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

# databases = conn.execute("""
#     SHOW DATABASES;
#     """)

# for db in databases.fetchall():
#     print(db)


