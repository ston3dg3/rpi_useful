# Python Script: dht11test.py
# Purpose: print temperature and humidity from dht11 sensor to the console for testing 
# -------------------------------

import Adafruit_DHT
import RPi.GPIO as GPIO
import time


sensor = Adafruit_DHT.DHT11
# select the right GPIO pin
pin = 17
# choose how frequently data is updated 
sleep_time = 2.0

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

while True:
	try:
		humid, temp = Adafruit_DHT.read(sensor,pin)
		print("temperature: {} C	humidity: {}% ".format(temp,humid))
		time.sleep(sleep_time)
	except RuntimeError as error:
		print(error.args[0])
		time.sleep(2.0)
		continue
	except Exception as error:
		break

