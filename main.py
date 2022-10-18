# python script to control a 8 pixel led strip raspberry pi with BCM GPIO

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

while True:
    GPIO.output(17, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(9, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(5, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(6, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(17, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(27, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(22, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(9, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(5, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(6, GPIO.LOW)
    time.sleep(0.05)

GPIO.cleanup()

# Here is the wiring diagram

# The script is pretty self explanatory. I have used the BCM GPIO numbering. The script turns on and off the LEDs in a loop. The LEDs are connected to the GPIO pins using a 220 ohm resistor. The LEDs are connected in series with the resistor. The resistor is used to limit the current through the LED and protect it from damage. If you don’t use the resistor, then the LEDs will burn out quickly. The script can be modified to control the LEDs in any pattern. The LEDs can be connected in parallel as well. The script can be modified to control the LEDs
