import RPi.GPIO as GPIO

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

try:
    dac = PWM_DAC(12, 500, 3.290, True)
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            dac.set_voltage(voltage)
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")
finally:
    dac.deinit()