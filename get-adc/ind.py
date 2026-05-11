
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

                    GPIO.output(self.gpio_bits, [0, 0, 0, 0, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 0, 0, 0, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 0, 0, 0, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 0, 0, 0, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 0, 0, 0, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 0, 0, 0, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 0, 0, 1, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 0, 0, 1, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 0, 0, 1, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 0, 0, 1, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 0, 0, 1, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 0, 0, 1, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 0, 1, 0, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 0, 1, 0, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 0, 1, 0, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 0, 1, 0, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 0, 1, 0, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 0, 1, 0, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 0, 1, 1, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 0, 1, 1, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 0, 1, 1, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 0, 1, 1, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 0, 1, 1, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 0, 1, 1, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 1, 0, 0, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 1, 0, 0, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 1, 0, 0, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 1, 0, 0, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 1, 0, 0, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 1, 0, 0, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 1, 0, 1, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 1, 0, 1, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 1, 0, 1, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 1, 0, 1, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 1, 0, 1, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 1, 0, 1, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 1, 1, 0, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 1, 1, 0, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 1, 1, 0, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 1, 1, 0, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 1, 1, 0, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 1, 1, 0, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 1, 1, 1, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 1, 1, 1, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 1, 1, 1, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [0, 1, 1, 1, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [0, 1, 1, 1, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [0, 1, 1, 1, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 0, 0, 0, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 0, 0, 0, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 0, 0, 0, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 0, 0, 0, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 0, 0, 0, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 0, 0, 0, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 0, 0, 1, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 0, 0, 1, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 0, 0, 1, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 0, 0, 1, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 0, 0, 1, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 0, 0, 1, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 0, 1, 0, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 0, 1, 0, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 0, 1, 0, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 0, 1, 0, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 0, 1, 0, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 0, 1, 0, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 0, 1, 1, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 0, 1, 1, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 0, 1, 1, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 0, 1, 1, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 0, 1, 1, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 0, 1, 1, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 1, 0, 0, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 1, 0, 0, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 1, 0, 0, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 1, 0, 0, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 1, 0, 0, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 1, 0, 0, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 1, 0, 1, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 1, 0, 1, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 1, 0, 1, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 1, 0, 1, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 1, 0, 1, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 1, 0, 1, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 1, 1, 0, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 1, 1, 0, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 1, 1, 0, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 1, 1, 0, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 1, 1, 0, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 1, 1, 0, 1, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 1, 1, 1, 0, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 1, 1, 1, 0, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 1, 1, 1, 0, 1, 1, 0])
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

                    GPIO.output(self.gpio_bits, [1, 1, 1, 1, 1, 1, 0, 0])
                    time.sleep(self.compare_time)
                    if GPIO.input(self.comp_gpio):

                        GPIO.output(self.gpio_bits, [1, 1, 1, 1, 1, 0, 1, 0])
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

                        GPIO.output(self.gpio_bits, [1, 1, 1, 1, 1, 1, 1, 0])
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
