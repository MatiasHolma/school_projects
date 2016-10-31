import RPi.GPIO as GPIO
import time


def vaihdavalot(vihrea, keltainen, punainen):
    GPIO.output(vihrea, 1)
    time.sleep(1)
    GPIO.output(vihrea, 0)
    GPIO.output(keltainen, 1)
    time.sleep(1)
    GPIO.output(keltainen, 0)
    GPIO.output(punainen, 1)
    time.sleep(1)

def vaihdavalot2(vihrea, keltainen, punainen):
    GPIO.output(vihrea, 1)
    time.sleep(1)
    GPIO.output(vihrea, 0)
    GPIO.output(punainen, 1)
    time.sleep(1)





LED=26
LED2=19
LED3=13
LEDD=21
LEDD2=20
LEDD3=16
PAINIKE=24

GPIO.setmode (GPIO.BCM)
GPIO.setup (LED, GPIO.OUT)
GPIO.setup (LED2, GPIO.OUT)
GPIO.setup (LED3, GPIO.OUT)
GPIO.setup (LEDD, GPIO.OUT)
GPIO.setup (LEDD2, GPIO.OUT)
GPIO.setup (LEDD3, GPIO.OUT)
GPIO.setup (PAINIKE, GPIO.IN)


loppu = time.time() + 30
while time.time() < loppu:
    GPIO.output(LED, 1)
    GPIO.output(LEDD3, 1)
    if (GPIO.input(PAINIKE)):
        vaihdavalot(LEDD3,LEDD2,LEDD)
        vaihdavalot2(LED,LED2,LED3)
        time.sleep(5)
        vaihdavalot2(LED3,LED2,LED)
        vaihdavalot(LEDD,LEDD2,LEDD3)
    time.sleep (0.1) # ilman tata prossukaytto 100%



GPIO.cleanup ()


