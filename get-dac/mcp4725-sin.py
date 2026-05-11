import smbus
import time
import numpy
import math

class MCP4725():
    def __init__(self, dynamic_range, address=0x61, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")

        if not (0 <= number <= 4095):
            print("Число выходит за разраядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def set_voltage(self, number):
        self.duty = number/self.dynamic_range
        self.set_number(int(4095*(number/self.dynamic_range)))


def sine(f, t):
    return (math.sin((2*math.pi*f*t)) + 1)/2

def wait_for_sampling_period(s_f):
    time.sleep(1/s_f)

amplitude = 3.0
sig_f = 1
s_f = 1000

try:
    dac = MCP4725(4.2, verbose=False)
    t = 0
    while True:
        dac.set_voltage(amplitude*sine(sig_f, t))
        wait_for_sampling_period(s_f)
        t += 1/s_f
finally:
    dac.deinit()