import RPi.GPIO as GPIO
import time
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
GPIO.setmode(GPIO.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

up, down = 9, 10
GPIO.setup([up, down], GPIO.IN)

num = 0
sleep_time = 0.2
while True:
    if GPIO.input(up):
        num = min(255, num + 1)
        print(num, dec2bin(num)[::-1])
        time.sleep(sleep_time)
    if GPIO.input(down):
        num = max(0, num - 1)
        print(num, dec2bin(num)[::-1])
        time.sleep(sleep_time)
    GPIO.output(leds, dec2bin(num)[::-1])