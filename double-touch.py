import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

leds = [16, 12, 25, 17, 27, 23, 22, 24]

up_button = 9
down_button = 10

for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, 0)

GPIO.setup(up_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(down_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

try:
    while True:
        if GPIO.input(up_button) and GPIO.input(down_button):
            num = 255
            print(num, dec2bin(num))
            time.sleep(sleep_time)
        elif GPIO.input(up_button):
            num = num + 1
            print(num, dec2bin(num))
            time.sleep(sleep_time)
        elif GPIO.input(down_button):
            num = num - 1
            print(num, dec2bin(num))
            time.sleep(sleep_time)
        
        if num > 255:
            num = 0
        elif num < 0:
            num = 255
        
        GPIO.output(leds, dec2bin(num))

except KeyboardInterrupt:
    GPIO.cleanup()