tab = "    "
bits = [0]*8
a = """
GPIO.output(self.gpio_bits, {});time.sleep(self.compare_time)
if GPIO.input(self.comp_gpio):
    {}
else:
    {}"""

def recursive(array, n = 0):
    if n == 8:
        return "return " + str(array)
    else:
        array1 = array.copy()
        array2 = array.copy()
        array2[n] = 1
        return a.format(array2, ("\n" + tab*(n+ 1)).join(recursive(array1, n = n + 1).split("\n")), ("\n" + tab*(n + 1)).join(recursive(array2, n = n + 1).split("\n")))

s = recursive([0]*8)
with open("/home/b04-506/Desktop/get-adc/ind.py", "w") as f:
    f.write(s)