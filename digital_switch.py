import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

button = 13
state = False

GPIO.setup(26, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

while True:
    if GPIO.input(button):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)
