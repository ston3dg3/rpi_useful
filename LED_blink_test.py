#!/usr/bin/python
# Script: LED_blink_test.sh
# Purpose: turn LED at GPIO pin 22 on and off after a short delay
# sets HIGH to pin 22 for one second then low for 1 second
# -------------------------------

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
