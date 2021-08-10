#!/usr/bin/env python3
# Script: ir_receiver_test.py
# Purpose: test the IR receiver at pin GPIO 23 by printing a count of received data
# -------------------------------

import RPi.GPIO as GPIO

IrPin = 23
count = 0

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(IrPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def cnt(ev=None):
	global count
	count += 1
	print ('Received infrared. cnt = ', count)

def loop():
	GPIO.add_event_detect(IrPin, GPIO.FALLING, cnt)
	while True:
		pass

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()


# UNFINISHED VERSION OF THIS CODE USING ANOTHER LIBRARY (gpiozero)
#from gpiozero import Button
#
#receiver = Button(17)
#except KeyboardInterrupt:
#	print("Ending program...")
