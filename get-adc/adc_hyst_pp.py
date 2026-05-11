import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import numpy as np


class R2R_DAC():
    def __init__(self, dynamic_range, compare_time=0.005, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.gpio_bits = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)
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


class R2R_DAC_indian():
    def __init__(self, dynamic_range, compare_time=0.005, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.gpio_bits = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def dec2bin(self, value):
        return [int(element) for element in bin(value)[2:].zfill(8)]

    # chfdytybt c byleccrbv rjljv
    def get_sc_voltage(self):

        GPIO.output(self.gpio_bits, [1, 0, 0, 0, 0, 0, 0, 0])
        time.sleep(self.compare_time)
        if GPIO.input(self.comp_gpio):

            GPIO.output(self.gpio_bits, [0, 1, 0, 0, 0, 0, 0, 0])
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio):

                GPIO.output(self.gpio_bits, [0, 0, 1, 0, 0, 0, 0, 0])
                time.sleep(self.compare_time)
                if GPIO.input(self.comp_gpio):

                    GPIO.output(self.gpio_bits, [0, 0, 0, 1, 0, 0, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 0, 0, 0, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        0, 0, 0, 0, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 0, 0, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 0, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 0, 0, 0, 0, 0]
                                    else:
                                        return [0, 0, 0, 0, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 0, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 0, 0, 0, 1, 0]
                                    else:
                                        return [0, 0, 0, 0, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 0, 0, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 0, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 0, 0, 1, 0, 0]
                                    else:
                                        return [0, 0, 0, 0, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 0, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 0, 0, 1, 1, 0]
                                    else:
                                        return [0, 0, 0, 0, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        0, 0, 0, 0, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 0, 0, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 0, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 0, 1, 0, 0, 0]
                                    else:
                                        return [0, 0, 0, 0, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 0, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 0, 1, 0, 1, 0]
                                    else:
                                        return [0, 0, 0, 0, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 0, 0, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 0, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 0, 1, 1, 0, 0]
                                    else:
                                        return [0, 0, 0, 0, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 0, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 0, 1, 1, 1, 0]
                                    else:
                                        return [0, 0, 0, 0, 1, 1, 1, 1]
                    else:

                        GPIO.output(self.gpio_bits, [0, 0, 0, 1, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        0, 0, 0, 1, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 0, 1, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 1, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 1, 0, 0, 0, 0]
                                    else:
                                        return [0, 0, 0, 1, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 1, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 1, 0, 0, 1, 0]
                                    else:
                                        return [0, 0, 0, 1, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 0, 1, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 1, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 1, 0, 1, 0, 0]
                                    else:
                                        return [0, 0, 0, 1, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 1, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 1, 0, 1, 1, 0]
                                    else:
                                        return [0, 0, 0, 1, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        0, 0, 0, 1, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 0, 1, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 1, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 1, 1, 0, 0, 0]
                                    else:
                                        return [0, 0, 0, 1, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 1, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 1, 1, 0, 1, 0]
                                    else:
                                        return [0, 0, 0, 1, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 0, 1, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 1, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 1, 1, 1, 0, 0]
                                    else:
                                        return [0, 0, 0, 1, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 0, 1, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 0, 1, 1, 1, 1, 0]
                                    else:
                                        return [0, 0, 0, 1, 1, 1, 1, 1]
                else:

                    GPIO.output(self.gpio_bits, [0, 0, 1, 1, 0, 0, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 0, 1, 0, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        0, 0, 1, 0, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 1, 0, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 0, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 0, 0, 0, 0, 0]
                                    else:
                                        return [0, 0, 1, 0, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 0, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 0, 0, 0, 1, 0]
                                    else:
                                        return [0, 0, 1, 0, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 1, 0, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 0, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 0, 0, 1, 0, 0]
                                    else:
                                        return [0, 0, 1, 0, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 0, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 0, 0, 1, 1, 0]
                                    else:
                                        return [0, 0, 1, 0, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        0, 0, 1, 0, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 1, 0, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 0, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 0, 1, 0, 0, 0]
                                    else:
                                        return [0, 0, 1, 0, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 0, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 0, 1, 0, 1, 0]
                                    else:
                                        return [0, 0, 1, 0, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 1, 0, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 0, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 0, 1, 1, 0, 0]
                                    else:
                                        return [0, 0, 1, 0, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 0, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 0, 1, 1, 1, 0]
                                    else:
                                        return [0, 0, 1, 0, 1, 1, 1, 1]
                    else:

                        GPIO.output(self.gpio_bits, [0, 0, 1, 1, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        0, 0, 1, 1, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 1, 1, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 1, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 1, 0, 0, 0, 0]
                                    else:
                                        return [0, 0, 1, 1, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 1, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 1, 0, 0, 1, 0]
                                    else:
                                        return [0, 0, 1, 1, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 1, 1, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 1, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 1, 0, 1, 0, 0]
                                    else:
                                        return [0, 0, 1, 1, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 1, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 1, 0, 1, 1, 0]
                                    else:
                                        return [0, 0, 1, 1, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        0, 0, 1, 1, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 1, 1, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 1, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 1, 1, 0, 0, 0]
                                    else:
                                        return [0, 0, 1, 1, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 1, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 1, 1, 0, 1, 0]
                                    else:
                                        return [0, 0, 1, 1, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 0, 1, 1, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 1, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 1, 1, 1, 0, 0]
                                    else:
                                        return [0, 0, 1, 1, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 0, 1, 1, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 0, 1, 1, 1, 1, 1, 0]
                                    else:
                                        return [0, 0, 1, 1, 1, 1, 1, 1]
            else:

                GPIO.output(self.gpio_bits, [0, 1, 1, 0, 0, 0, 0, 0])
                time.sleep(self.compare_time)
                if GPIO.input(self.comp_gpio):

                    GPIO.output(self.gpio_bits, [0, 1, 0, 1, 0, 0, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 1, 0, 0, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        0, 1, 0, 0, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 0, 0, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 0, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 0, 0, 0, 0, 0]
                                    else:
                                        return [0, 1, 0, 0, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 0, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 0, 0, 0, 1, 0]
                                    else:
                                        return [0, 1, 0, 0, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 0, 0, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 0, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 0, 0, 1, 0, 0]
                                    else:
                                        return [0, 1, 0, 0, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 0, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 0, 0, 1, 1, 0]
                                    else:
                                        return [0, 1, 0, 0, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        0, 1, 0, 0, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 0, 0, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 0, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 0, 1, 0, 0, 0]
                                    else:
                                        return [0, 1, 0, 0, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 0, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 0, 1, 0, 1, 0]
                                    else:
                                        return [0, 1, 0, 0, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 0, 0, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 0, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 0, 1, 1, 0, 0]
                                    else:
                                        return [0, 1, 0, 0, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 0, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 0, 1, 1, 1, 0]
                                    else:
                                        return [0, 1, 0, 0, 1, 1, 1, 1]
                    else:

                        GPIO.output(self.gpio_bits, [0, 1, 0, 1, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        0, 1, 0, 1, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 0, 1, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 1, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 1, 0, 0, 0, 0]
                                    else:
                                        return [0, 1, 0, 1, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 1, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 1, 0, 0, 1, 0]
                                    else:
                                        return [0, 1, 0, 1, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 0, 1, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 1, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 1, 0, 1, 0, 0]
                                    else:
                                        return [0, 1, 0, 1, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 1, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 1, 0, 1, 1, 0]
                                    else:
                                        return [0, 1, 0, 1, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        0, 1, 0, 1, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 0, 1, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 1, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 1, 1, 0, 0, 0]
                                    else:
                                        return [0, 1, 0, 1, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 1, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 1, 1, 0, 1, 0]
                                    else:
                                        return [0, 1, 0, 1, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 0, 1, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 1, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 1, 1, 1, 0, 0]
                                    else:
                                        return [0, 1, 0, 1, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 0, 1, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 0, 1, 1, 1, 1, 0]
                                    else:
                                        return [0, 1, 0, 1, 1, 1, 1, 1]
                else:

                    GPIO.output(self.gpio_bits, [0, 1, 1, 1, 0, 0, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 1, 1, 0, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        0, 1, 1, 0, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 1, 0, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 0, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 0, 0, 0, 0, 0]
                                    else:
                                        return [0, 1, 1, 0, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 0, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 0, 0, 0, 1, 0]
                                    else:
                                        return [0, 1, 1, 0, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 1, 0, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 0, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 0, 0, 1, 0, 0]
                                    else:
                                        return [0, 1, 1, 0, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 0, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 0, 0, 1, 1, 0]
                                    else:
                                        return [0, 1, 1, 0, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        0, 1, 1, 0, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 1, 0, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 0, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 0, 1, 0, 0, 0]
                                    else:
                                        return [0, 1, 1, 0, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 0, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 0, 1, 0, 1, 0]
                                    else:
                                        return [0, 1, 1, 0, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 1, 0, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 0, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 0, 1, 1, 0, 0]
                                    else:
                                        return [0, 1, 1, 0, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 0, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 0, 1, 1, 1, 0]
                                    else:
                                        return [0, 1, 1, 0, 1, 1, 1, 1]
                    else:

                        GPIO.output(self.gpio_bits, [0, 1, 1, 1, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        0, 1, 1, 1, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 1, 1, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 1, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 1, 0, 0, 0, 0]
                                    else:
                                        return [0, 1, 1, 1, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 1, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 1, 0, 0, 1, 0]
                                    else:
                                        return [0, 1, 1, 1, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 1, 1, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 1, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 1, 0, 1, 0, 0]
                                    else:
                                        return [0, 1, 1, 1, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 1, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 1, 0, 1, 1, 0]
                                    else:
                                        return [0, 1, 1, 1, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        0, 1, 1, 1, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 1, 1, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 1, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 1, 1, 0, 0, 0]
                                    else:
                                        return [0, 1, 1, 1, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 1, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 1, 1, 0, 1, 0]
                                    else:
                                        return [0, 1, 1, 1, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            0, 1, 1, 1, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 1, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 1, 1, 1, 0, 0]
                                    else:
                                        return [0, 1, 1, 1, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                0, 1, 1, 1, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [0, 1, 1, 1, 1, 1, 1, 0]
                                    else:
                                        return [0, 1, 1, 1, 1, 1, 1, 1]
        else:

            GPIO.output(self.gpio_bits, [1, 1, 0, 0, 0, 0, 0, 0])
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio):

                GPIO.output(self.gpio_bits, [1, 0, 1, 0, 0, 0, 0, 0])
                time.sleep(self.compare_time)
                if GPIO.input(self.comp_gpio):

                    GPIO.output(self.gpio_bits, [1, 0, 0, 1, 0, 0, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 0, 0, 0, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        1, 0, 0, 0, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 0, 0, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 0, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 0, 0, 0, 0, 0]
                                    else:
                                        return [1, 0, 0, 0, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 0, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 0, 0, 0, 1, 0]
                                    else:
                                        return [1, 0, 0, 0, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 0, 0, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 0, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 0, 0, 1, 0, 0]
                                    else:
                                        return [1, 0, 0, 0, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 0, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 0, 0, 1, 1, 0]
                                    else:
                                        return [1, 0, 0, 0, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        1, 0, 0, 0, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 0, 0, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 0, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 0, 1, 0, 0, 0]
                                    else:
                                        return [1, 0, 0, 0, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 0, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 0, 1, 0, 1, 0]
                                    else:
                                        return [1, 0, 0, 0, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 0, 0, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 0, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 0, 1, 1, 0, 0]
                                    else:
                                        return [1, 0, 0, 0, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 0, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 0, 1, 1, 1, 0]
                                    else:
                                        return [1, 0, 0, 0, 1, 1, 1, 1]
                    else:

                        GPIO.output(self.gpio_bits, [1, 0, 0, 1, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        1, 0, 0, 1, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 0, 1, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 1, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 1, 0, 0, 0, 0]
                                    else:
                                        return [1, 0, 0, 1, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 1, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 1, 0, 0, 1, 0]
                                    else:
                                        return [1, 0, 0, 1, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 0, 1, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 1, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 1, 0, 1, 0, 0]
                                    else:
                                        return [1, 0, 0, 1, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 1, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 1, 0, 1, 1, 0]
                                    else:
                                        return [1, 0, 0, 1, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        1, 0, 0, 1, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 0, 1, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 1, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 1, 1, 0, 0, 0]
                                    else:
                                        return [1, 0, 0, 1, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 1, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 1, 1, 0, 1, 0]
                                    else:
                                        return [1, 0, 0, 1, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 0, 1, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 1, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 1, 1, 1, 0, 0]
                                    else:
                                        return [1, 0, 0, 1, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 0, 1, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 0, 1, 1, 1, 1, 0]
                                    else:
                                        return [1, 0, 0, 1, 1, 1, 1, 1]
                else:

                    GPIO.output(self.gpio_bits, [1, 0, 1, 1, 0, 0, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 0, 1, 0, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        1, 0, 1, 0, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 1, 0, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 0, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 0, 0, 0, 0, 0]
                                    else:
                                        return [1, 0, 1, 0, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 0, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 0, 0, 0, 1, 0]
                                    else:
                                        return [1, 0, 1, 0, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 1, 0, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 0, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 0, 0, 1, 0, 0]
                                    else:
                                        return [1, 0, 1, 0, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 0, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 0, 0, 1, 1, 0]
                                    else:
                                        return [1, 0, 1, 0, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        1, 0, 1, 0, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 1, 0, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 0, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 0, 1, 0, 0, 0]
                                    else:
                                        return [1, 0, 1, 0, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 0, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 0, 1, 0, 1, 0]
                                    else:
                                        return [1, 0, 1, 0, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 1, 0, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 0, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 0, 1, 1, 0, 0]
                                    else:
                                        return [1, 0, 1, 0, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 0, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 0, 1, 1, 1, 0]
                                    else:
                                        return [1, 0, 1, 0, 1, 1, 1, 1]
                    else:

                        GPIO.output(self.gpio_bits, [1, 0, 1, 1, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        1, 0, 1, 1, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 1, 1, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 1, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 1, 0, 0, 0, 0]
                                    else:
                                        return [1, 0, 1, 1, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 1, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 1, 0, 0, 1, 0]
                                    else:
                                        return [1, 0, 1, 1, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 1, 1, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 1, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 1, 0, 1, 0, 0]
                                    else:
                                        return [1, 0, 1, 1, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 1, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 1, 0, 1, 1, 0]
                                    else:
                                        return [1, 0, 1, 1, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        1, 0, 1, 1, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 1, 1, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 1, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 1, 1, 0, 0, 0]
                                    else:
                                        return [1, 0, 1, 1, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 1, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 1, 1, 0, 1, 0]
                                    else:
                                        return [1, 0, 1, 1, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 0, 1, 1, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 1, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 1, 1, 1, 0, 0]
                                    else:
                                        return [1, 0, 1, 1, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 0, 1, 1, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 0, 1, 1, 1, 1, 1, 0]
                                    else:
                                        return [1, 0, 1, 1, 1, 1, 1, 1]
            else:

                GPIO.output(self.gpio_bits, [1, 1, 1, 0, 0, 0, 0, 0])
                time.sleep(self.compare_time)
                if GPIO.input(self.comp_gpio):

                    GPIO.output(self.gpio_bits, [1, 1, 0, 1, 0, 0, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 1, 0, 0, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        1, 1, 0, 0, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 0, 0, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 0, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 0, 0, 0, 0, 0]
                                    else:
                                        return [1, 1, 0, 0, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 0, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 0, 0, 0, 1, 0]
                                    else:
                                        return [1, 1, 0, 0, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 0, 0, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 0, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 0, 0, 1, 0, 0]
                                    else:
                                        return [1, 1, 0, 0, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 0, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 0, 0, 1, 1, 0]
                                    else:
                                        return [1, 1, 0, 0, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        1, 1, 0, 0, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 0, 0, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 0, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 0, 1, 0, 0, 0]
                                    else:
                                        return [1, 1, 0, 0, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 0, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 0, 1, 0, 1, 0]
                                    else:
                                        return [1, 1, 0, 0, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 0, 0, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 0, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 0, 1, 1, 0, 0]
                                    else:
                                        return [1, 1, 0, 0, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 0, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 0, 1, 1, 1, 0]
                                    else:
                                        return [1, 1, 0, 0, 1, 1, 1, 1]
                    else:

                        GPIO.output(self.gpio_bits, [1, 1, 0, 1, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        1, 1, 0, 1, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 0, 1, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 1, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 1, 0, 0, 0, 0]
                                    else:
                                        return [1, 1, 0, 1, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 1, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 1, 0, 0, 1, 0]
                                    else:
                                        return [1, 1, 0, 1, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 0, 1, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 1, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 1, 0, 1, 0, 0]
                                    else:
                                        return [1, 1, 0, 1, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 1, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 1, 0, 1, 1, 0]
                                    else:
                                        return [1, 1, 0, 1, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        1, 1, 0, 1, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 0, 1, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 1, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 1, 1, 0, 0, 0]
                                    else:
                                        return [1, 1, 0, 1, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 1, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 1, 1, 0, 1, 0]
                                    else:
                                        return [1, 1, 0, 1, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 0, 1, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 1, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 1, 1, 1, 0, 0]
                                    else:
                                        return [1, 1, 0, 1, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 0, 1, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 0, 1, 1, 1, 1, 0]
                                    else:
                                        return [1, 1, 0, 1, 1, 1, 1, 1]
                else:

                    GPIO.output(self.gpio_bits, [1, 1, 1, 1, 0, 0, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 1, 1, 0, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        1, 1, 1, 0, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 1, 0, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 0, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 0, 0, 0, 0, 0]
                                    else:
                                        return [1, 1, 1, 0, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 0, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 0, 0, 0, 1, 0]
                                    else:
                                        return [1, 1, 1, 0, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 1, 0, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 0, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 0, 0, 1, 0, 0]
                                    else:
                                        return [1, 1, 1, 0, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 0, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 0, 0, 1, 1, 0]
                                    else:
                                        return [1, 1, 1, 0, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        1, 1, 1, 0, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 1, 0, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 0, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 0, 1, 0, 0, 0]
                                    else:
                                        return [1, 1, 1, 0, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 0, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 0, 1, 0, 1, 0]
                                    else:
                                        return [1, 1, 1, 0, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 1, 0, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 0, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 0, 1, 1, 0, 0]
                                    else:
                                        return [1, 1, 1, 0, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 0, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 0, 1, 1, 1, 0]
                                    else:
                                        return [1, 1, 1, 0, 1, 1, 1, 1]
                    else:

                        GPIO.output(self.gpio_bits, [1, 1, 1, 1, 1, 0, 0, 0])
                        time.sleep(self.compare_time)
                        if GPIO.input(self.comp_gpio):

                            GPIO.output(self.gpio_bits, [
                                        1, 1, 1, 1, 0, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 1, 1, 0, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 1, 0, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 1, 0, 0, 0, 0]
                                    else:
                                        return [1, 1, 1, 1, 0, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 1, 0, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 1, 0, 0, 1, 0]
                                    else:
                                        return [1, 1, 1, 1, 0, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 1, 1, 0, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 1, 0, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 1, 0, 1, 0, 0]
                                    else:
                                        return [1, 1, 1, 1, 0, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 1, 0, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 1, 0, 1, 1, 0]
                                    else:
                                        return [1, 1, 1, 1, 0, 1, 1, 1]
                        else:

                            GPIO.output(self.gpio_bits, [
                                        1, 1, 1, 1, 1, 1, 0, 0])
                            time.sleep(self.compare_time)
                            if GPIO.input(self.comp_gpio):

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 1, 1, 1, 0, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 1, 1, 0, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 1, 1, 0, 0, 0]
                                    else:
                                        return [1, 1, 1, 1, 1, 0, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 1, 1, 0, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 1, 1, 0, 1, 0]
                                    else:
                                        return [1, 1, 1, 1, 1, 0, 1, 1]
                            else:

                                GPIO.output(self.gpio_bits, [
                                            1, 1, 1, 1, 1, 1, 1, 0])
                                time.sleep(self.compare_time)
                                if GPIO.input(self.comp_gpio):

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 1, 1, 1, 0, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 1, 1, 1, 0, 0]
                                    else:
                                        return [1, 1, 1, 1, 1, 1, 0, 1]
                                else:

                                    GPIO.output(self.gpio_bits, [
                                                1, 1, 1, 1, 1, 1, 1, 1])
                                    time.sleep(self.compare_time)
                                    if GPIO.input(self.comp_gpio):
                                        return [1, 1, 1, 1, 1, 1, 1, 0]
                                    else:
                                        return [1, 1, 1, 1, 1, 1, 1, 1]


def plot_hyst(max_time, sleep_time, max_voltage):
    try:
        adc = R2R_DAC(max_time)
        voltage = []
        t = []
        zero_time = time.time()
        while time.time() - zero_time < max_time:
            last_time = time.time_ns()
            voltage.append(adc.get_sc_voltage())
            t.append((time.time_ns() - last_time)*10**(-6))
            time.sleep(sleep_time)

        plt.figure(figsize=(10, 6))
        counts, bins = np.histogram(t, bins=150)
        plt.hist(bins[:-1], bins, weights=counts)

        adc = R2R_DAC_indian(max_time)
        voltage = []
        t = []
        zero_time = time.time()
        while time.time() - zero_time < max_time:
            last_time = time.time_ns()
            voltage.append(adc.get_sc_voltage())
            t.append((time.time_ns() - last_time)*10**(-6))
            time.sleep(sleep_time)

        counts, bins = np.histogram(t, bins=150)
        plt.hist(bins[:-1], bins, weights=counts)
        plt.title("Гистограмма периодов дискретизации измерени")
        plt.xlabel("Время, мс")
        plt.ylabel("Число вхождений, 1")
        plt.show()
    finally:
        adc.deinit()


plot_hyst(5, 0, 3.3)
