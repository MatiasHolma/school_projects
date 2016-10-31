import picamera
import datetime
import RPi.GPIO as GPIO
import time

camera = picamera.PiCamera()


LIIKE = 18
GPIO.setmode (GPIO.BCM)
GPIO.setup (LIIKE, GPIO.IN)

loppu = time.time() + 10
while time.time() < loppu:
    if (GPIO.input(LIIKE)):
        camera.capture(str(datetime.datetime.now())+'image.jpg')
        time.sleep(1)
    time.sleep(1)
GPIO.cleanup ()
