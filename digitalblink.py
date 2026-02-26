import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(9, GPIO.IN)
period = 0.2
i=0

while 1:
    time.sleep(period)
    i = not i 
    GPIO.output(26, i)