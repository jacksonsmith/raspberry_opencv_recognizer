import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)   
GPIO.setwarnings(False)         
GPIO.setup(40, GPIO.OUT)   

  
while(1):                     
 GPIO.output(40, 1)             
