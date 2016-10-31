import picamera
import datetime
import time

camera = picamera.PiCamera()
camera.capture('/home/pi/'+str(datetime.datetime.now())+'image.jpg')
