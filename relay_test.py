#!/usr/bin/python
# Script: relay.py
# Purpose: turn on relay when (pin) is set to HIGH

import RPi.GPIO as GPIO
import time

channel = 27

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def pin_on(pin):
	GPIO.output(pin, GPIO.HIGH)

def pin_off(pin):
	GPIO.output(pin, GPIO.LOW)

if __name__ == '__main__':
	try:
		pin_on(channel)
		time.sleep(5)
		pin_off(channel)
		time.sleep(1)
		GPIO.cleanup()
	except KeyboardInterrupt:
		GPIO.cleanup()
