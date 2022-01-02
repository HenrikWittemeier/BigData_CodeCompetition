import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields
from flask_cors import CORS, cross_origin
from datetime import datetime
import requests
import json
import time
from datetime import datetime
import re


app = Flask("foo")
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://codecompetitor:extremesafepassword@database:3306/codecompetition'
app.config['SECRET_KEY'] = 'Th1s1ss3cr3t'

db = SQLAlchemy(app)
ma = Marshmallow(app)

## Machine
class Race(db.Model):
    __tablename__ = 'race'
    id = db.Column(db.Integer, primary_key=True)
    race_created = db.Column(db.Date)
    race_driven = db.Column(db.DateTime)
    track_id = db.Column(db.Integer)
    challenger = db.Column(db.Integer)
    opponent = db.Column(db.Integer)
    money = db.Column(db.Integer)
    fuel_consumption = db.Column(db.Numeric)   
    winner = db.Column(db.Integer)
    status = db.Column(db.String(8))
    forecast_sunny = db.Column(db.Integer)
    forecat_rainy = db.Column(db.Integer)
    forecast_thundery = db.Column(db.Integer)
    forecast_snowy = db.Column(db.Integer)
    weather = db.Column(db.Integer)



    def __init__(self, id,race_created,race_driven,track_id,challenger,opponent,money,fuel_consumption,winner,status,forecast_sunny,forecat_rainy,forecast_thundery,forecast_snowy,weather):
        self.id = id
        self.race_created = race_created
        self.race_driven = race_driven
        self.track_id = track_id
        self.challenger = challenger
        self.opponent = opponent
        self.money = money
        self.fuel_consumption = fuel_consumption
        self.winner = winner
        self.status = status
        self.forecast_sunny = forecast_sunny
        self.forecat_rainy = forecat_rainy
        self.forecast_thundery = forecast_thundery
        self.forecast_snowy = forecast_snowy
        self.weather = weather
        


racescsv = open('races.csv', 'r')
Lines = racescsv.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    m = re.search(r'(\d+);([\w.]+);([\w.: -]+);(\d+);(\d+);(\d+);(\d+);([\d.]+);(\d+);(\w+);"a:4:{s:5:""sunny"";i:(\d+);s:5:""rainy"";i:(\d+);s:8:""thundery"";i:(\d+);s:5:""snowy"";i:(\d+);}";(\w+)?', line.strip())
    if not m:
        print("Line{}: {}".format(count, line.strip()))
        print("Found corrupt Data")
        continue
    
    race_driven = None

    if m.group(10) == "finished":
        race_driven = datetime.strptime(m.group(3),"%d.%m.%Y %H:%M")
    else:
        race_driven = datetime(1,1,1,1,1,1)
    race_created = datetime.strptime(m.group(2),"%d.%m.%Y")
    race_created = datetime.strftime(race_created,"%y-%m-%d")
    race_driven = datetime.strftime(race_driven,"%y-%m-%d %H:%M:%S")
    race = Race(m.group(1),race_created,race_driven,m.group(4),m.group(5),m.group(6),m.group(7),m.group(8),m.group(9),m.group(10),m.group(11),m.group(12),m.group(13),m.group(14),m.group(15) or "NaN")
    db.session.add(race)
db.session.commit()