#python script to control a 8 pixel led strip raspberry pi with BCM GPIO

# Import modules
import RPi.GPIO as GPIO
import time
import random

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
GPIO.setup(10, GPIO.OUT)

# Define functions
def red():
    GPIO.output(18, GPIO.HIGH)

def main():
    while True:
        red()

if __name__ == '__main__':
    main()

# End of script

# Run the script
# chmod +x main.py
# ./main.py
