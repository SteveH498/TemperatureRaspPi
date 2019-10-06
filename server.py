from flask import Flask
from flask import jsonify
import sqlite3

app = Flask(__name__)

@app.route("/readings", methods = ['GET'])
def readings():
	# Open DB for sensor readings
	conn = sqlite3.connect('temperature.db')
	c = conn.cursor()
	c.execute('SELECT * FROM readings') 
	readings = c.fetchall()
	conn.close()	
	return jsonify(readings)
	
@app.route("/readings/today", methods = ['GET'])
def readings_today():
	# Open DB for sensor readings
	conn = sqlite3.connect('temperature.db')
	c = conn.cursor()
	c.execute('SELECT * FROM readings WHERE date(timestamp) = date("now")') 	
	readings_today = c.fetchall()
	conn.close()
	return jsonify(readings_today)
