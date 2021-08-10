#!/usr/bin/env python3

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


#from gpiozero import Button
#
#receiver = Button(17)
#except KeyboardInterrupt:
#	print("Ending program...")
