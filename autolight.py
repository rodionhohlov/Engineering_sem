import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(6, GPIO.IN)

while 1:
    i = not GPIO.input(6)
    GPIO.output(26, i)