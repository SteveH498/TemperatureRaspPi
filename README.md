# TemperatureRaspPi
Reading Temperature and Humidity DHT1 sensor

Start sensor readings script:
python3 sensor_readings.py

Start REST server:
env FLASK_APP=server.py flask run --host=0.0.0.0

Server runs with port 5000, e.g.

http://192.168.178.40:5000/readings
http://192.168.178.40:5000/readings/today
