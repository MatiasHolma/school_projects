import RPi.GPIO as GPIO
import time

LED = 17
TUNNISTIN = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(TUNNISTIN, GPIO.IN)

loppu = time.time() + 10

while time.time() < loppu:
    GPIO.output(LED, GPIO.input(TUNNISTIN))
    time.sleep(0.1)

GPIO.cleanup()
    
