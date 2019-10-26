
python3 /home/pi/Desktop/TemperatureRaspPi/sensor_readings.py &
env FLASK_APP=/home/pi/Desktop/TemperatureRaspPi/server.py flask run --host=0.0.0.0 &
/etc/init.d/nginx start &
