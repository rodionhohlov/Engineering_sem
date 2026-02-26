import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(13, GPIO.IN)
ledstate = 0

while 1:
    if GPIO.input(13):
        ledstate = not (ledstate)
        GPIO.output(26, ledstate)
        time.sleep(0.2)