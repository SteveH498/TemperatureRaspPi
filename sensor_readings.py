#!/usr/bin/python3

import Adafruit_DHT
import datetime
import time
import sqlite3

# Create/Open DB for sensor readings
conn = sqlite3.connect('/home/pi/Desktop/TemperatureRaspPi/temperature.db')
c = conn.cursor()

# Create DB table
c.execute('''CREATE TABLE IF NOT EXISTS readings (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, temperature REAL, humidity REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL)''')


# We are using the DHT11 version of the temperature and humidity sensor here
sensor = Adafruit_DHT.DHT11

# Pin 7 = BCM 4
pin = 4

while True:

	# Try to grab a sensor reading.  Use the read_retry method which will retry up
	# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

	if humidity is not None and temperature is not None:
	    now_utc = datetime.datetime.utcnow()
	    print('Temp={0:0.1f}*  Humidity={1:0.1f}% Time={2}'.format(temperature, humidity, now_utc))
	else:
	    print('Failed to get reading. Try again!')

	# Insert a row of data
	c.execute("INSERT INTO readings (temperature, humidity) VALUES ({0:0.1f},{1:0.1f})".format(temperature, humidity))

	# Save (commit) the changes
	conn.commit()

	# Wait for one minute until next reading...
	time.sleep(60) 
