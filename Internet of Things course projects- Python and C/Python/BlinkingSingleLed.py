import RPi.GPIO as GPIO
import time

LED = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

for i in range (0, 10):
    GPIO.output(LED, 1)
    time.sleep(1)
    GPIO.output(LED,0)
    time.sleep(1)
GPIO.cleanup()
    
