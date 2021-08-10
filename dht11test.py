import Adafruit_DHT
import RPi.GPIO as GPIO
import time


sensor = Adafruit_DHT.DHT11
pin = 17
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

