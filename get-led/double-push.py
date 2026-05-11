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
cooldown = 0.05
sleep_time = 0.2
elapsed = -1
last_up = -1
last_down = -1
while True:
    now = time.time()
    if GPIO.input(up) and (now - elapsed) >= sleep_time:
        num = num + 1
        print(num, dec2bin(num)[::-1])
        elapsed = time.time()
    if GPIO.input(down) and (now - elapsed) >= sleep_time:
        num = max(0, num - 1)
        print(num, dec2bin(num)[::-1])
        elapsed = time.time()

    if GPIO.input(up):
        last_up = time.time()
    if GPIO.input(down):
        last_down = time.time()

    if last_up != -1 and last_down != -1 and abs(last_up - last_down) < cooldown and (now - elapsed) >= sleep_time:
        num = 255
        elapsed = time.time()

    num = min(255, max(num, 0))

    GPIO.output(leds, dec2bin(num)[::-1])