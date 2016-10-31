import RPi.GPIO as GPIO
import time

LED=4

GPIO.setmode (GPIO.BCM)
GPIO.setup (LED, GPIO.OUT)
GPIO.output(LED, 1)
time.sleep(2)
GPIO.output(LED, 0)
GPIO.cleanup ()


