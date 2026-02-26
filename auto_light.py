import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(13, GPIO.IN)
i = 0

while 1:
    if GPIO.input(13):
        i = not i
        GPIO.output(26, i)
        time.sleep(0.2)