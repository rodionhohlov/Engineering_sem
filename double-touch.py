import RPi.GPIO as GPIO
import time 

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def printleds(leds, bin_num):
    for i in range (len(leds)):
        GPIO.output(leds[i], bin_num[i])

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]

GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)


for i in leds:
    GPIO.setup(i, GPIO.OUT)

num = 0
sleep_time = 0.2
while 1:
    if GPIO.input(up) and GPIO.input(down):
        num = 255
        
    elif GPIO.input(up):
        num = num + 1
        
    elif GPIO.input(down):
        num = num - 1
    
    print(num, dec2bin(num % 256))
    time.sleep(sleep_time)
    printleds(leds, dec2bin(num % 256))
