from gpiozero import Buzzer
from gpiozero import MotionSensor

buzz = Buzzer(17)
pir = MotionSensor(4)
buzz.off()

while True:
	pir.wait_for_motion()
	print("Motionb Deceted")
	buzz.on()
	pir.wait_for_no_motion()
	buzz.off()
	print("Motion stopped")
