#!/usr/bin/python3

import Adafruit_DHT
import time
from datetime import datetime

# We are using the DHT11 version of the temperature and humidity sensor here
sensor = Adafruit_DHT.DHT11

# Pin 7 = BCM 4
pin = 4

while True:

	# Try to grab a sensor reading.  Use the read_retry method which will retry up
	# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

	if humidity is not None and temperature is not None:
	    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
	else:
	    print('Failed to get reading. Try again!')

	# Wait for one minute until next reading...
	time.sleep(60) 
