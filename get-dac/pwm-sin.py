import RPi.GPIO as GPIO
import time
import numpy
import math

class PWM_DAC():
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.duty = 0.0
        self.pwm.start(self.duty)

    def set_voltage(self, number):
        self.duty = 100*number/self.dynamic_range
        self.pwm.ChangeDutyCycle(self.duty)

def sine(f, t):
    return (math.sin((2*math.pi*f*t)) + 1)/2

def wait_for_sampling_period(s_f):
    time.sleep(1/s_f)

amplitude = 3.0
sig_f = 1
s_f = 1000

try:
    dac = PWM_DAC(12, 500, 3.183, True)
    t = 0
    while True:
        dac.set_voltage(amplitude*sine(sig_f, t))
        wait_for_sampling_period(s_f)
        t += 1/s_f
finally:
    dac.deinit()