import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)

state = 0
period = 1.0

while True:
    GPIO.output(26, state)
    state = not state
    time.sleep(period)


