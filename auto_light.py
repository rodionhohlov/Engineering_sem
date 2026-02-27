import RPi.GPIO as GPIO
import time

LED_PIN = 26
LIGHT_SENSOR_PIN = 18  

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)

while True:
    if GPIO.input(DIGITAL_SENSOR_PIN) == GPIO.LOW:
        GPIO.output(LED_PIN, GPIO.HIGH)  
        
    else:
        GPIO.output(LED_PIN, GPIO.LOW)   
    
    time.sleep(0.2)  
