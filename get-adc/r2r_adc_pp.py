import RPi.GPIO as GPIO
import time

class R2R_DAC():
    def __init__(self, dynamic_range, compare_time = 0.1, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
            
        self.gpio_bits = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)


    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()


    def dec2bin(self, value):
        return [int(element) for element in bin(value)[2:].zfill(8)]


    def get_sc_voltage(self):
        a = [0]*8
        for i in range(8):
            a[i] = 1
            GPIO.output(self.gpio_bits, a)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio):
                a[i] = 0
        return self.dynamic_range*int("".join(map(str, a)), 2)/(2**8)

try:
    adc = R2R_DAC(3.3)
    while True:
        print("Напряжение:", adc.get_sc_voltage())
        time.sleep(1)
finally:
    adc.deinit()
