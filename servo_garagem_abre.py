import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)

print("opa")

p = GPIO.PWM(38, 50)  # channel=12 frequency=50Hz
p.start(0)

for dc in range(0, 30, 1):
	p.ChangeDutyCycle(dc)
        time.sleep(0.1)
p.stop()
GPIO.cleanup()
