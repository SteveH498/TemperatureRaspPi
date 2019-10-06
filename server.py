from flask import Flask
from flask import jsonify
import sqlite3

app = Flask(__name__)



@app.route("/readings", methods = ['GET'])
def hello():
	# Open DB for sensor readings
	conn = sqlite3.connect('temperature.db')
	c = conn.cursor()
	c.execute('SELECT * FROM readings') 	
	return jsonify(c.fetchall())
	
