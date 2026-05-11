import RPi.GPIO as GPIO
import time
import numpy
import math

class R2R_DAC():
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def dec2bin(self, value):
        return [int(element) for element in bin(value)[2:].zfill(8)]

    def voltage_to_number(self, voltage):
        if not (0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение не входит в динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
                print("Устанавливаем в 0.0 В")
            return 0
        return int(voltage/self.dynamic_range*255)

    def set_voltage(self, number):
        GPIO.output(self.gpio_bits, self.dec2bin(self.voltage_to_number(number)))

    def set_number(self, number):
        if not (0 <= number <= 255):
            if self.verbose:
                print("плохое значение")
            GPIO.output(self.gpio_bits, number)

def sine(f, t):
    return (math.sin((2*math.pi*f*t)) + 1)/2

def wait_for_sampling_period(s_f):
    time.sleep(1/s_f)

amplitude = 3.0
sig_f = 1
s_f = 1000

try:
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
    t = 0
    while True:
        dac.set_voltage(amplitude*sine(sig_f, t))
        wait_for_sampling_period(s_f)
        t += 1/s_f
finally:
    dac.deinit()