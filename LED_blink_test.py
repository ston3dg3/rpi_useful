#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

while True:
	try:
		GPIO.output(22, True)
		time.sleep(1)
		GPIO.output(22, False)
		time.sleep(1)
	except KeyboardInterrupt:
		GPIO.output(22, False)
		break
