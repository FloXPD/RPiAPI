#python script to control a 8 pixel led strip raspberry pi with BCM GPIOzero

import time
import gpiozero
from gpiozero import LEDBoard
from gpiozero.tools import random_values

#8 pixel led strip
leds = LEDBoard(23, 24, 25, 8, 7, 1, 12, 16, pwm=True)

try:
    while True:
        leds.value = (0, 0, 0, 0, 0, 0, 0, 0)
        time.sleep(0.1)
        leds.value = (1, 0, 0, 0, 0, 0, 0, 0)
        time.sleep(0.1)
        leds.value = (1, 1, 0, 0, 0, 0, 0, 0)
        time.sleep(0.1)
        leds.value = (1, 1, 1, 0, 0, 0, 0, 0)
        time.sleep(0.1)
        leds.value = (1, 1, 1, 1, 0, 0, 0, 0)
        time.sleep(0.1)
        leds.value = (1, 1, 1, 1, 1, 0, 0, 0)
        time.sleep(0.1)
        leds.value = (1, 1, 1, 1, 1, 1, 0, 0)
        time.sleep(0.1)
        leds.value = (1, 1, 1, 1, 1, 1, 1, 0)
        time.sleep(0.1)
        leds.value = (1, 1, 1, 1, 1, 1, 1, 1)
        time.sleep(0.1)
        leds.value = (1, 1, 1, 1, 1, 1, 1, 0)
        time.sleep(0.1)
        leds.value = (1, 1, 1, 1, 1, 1, 0, 0)
        time.sleep(0.1)
        leds.value = (1, 1, 1, 1, 1, 0, 0, 0)
        time.sleep(0.1)