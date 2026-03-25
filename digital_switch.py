import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 26

GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0)

button = 13

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

state = 0

try:
    while True:
        if GPIO.input(button):
            state = not state
            GPIO.output(led, state)
            time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()