import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

p = GPIO.PWM(40, 50)  # channel=12 frequency=50Hz
p.start(0)
for dc in range(20, 40, 1):
	p.ChangeDutyCycle(dc)
	time.sleep(0.1)
p.stop()
GPIO.cleanup()
