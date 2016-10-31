import RPi.GPIO as GPIO
import time

LED = 17
NAPPI = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(NAPPI, GPIO.IN)

loppu = time.time() + 10

while time.time() < loppu:
    GPIO.output(LED, GPIO.input(NAPPI))
    print(str(GPIO.input(NAPPI))
    time.sleep(0.1)

GPIO.cleanup()
    
