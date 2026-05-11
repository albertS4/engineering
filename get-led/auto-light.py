import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)

transistor = 6
GPIO.setup(transistor, GPIO.IN)

state = 1
while True:
    GPIO.output(led, not GPIO.input(transistor))