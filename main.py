# Raspberry Pi API for a 8x1 LED Matrix

import time
import RPi.GPIO as GPIO
import sys

# Pin Definitions
output_pin = 17  # BOARD pin 11, BCM pin 17

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(output_pin, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(output_pin, GPIO.HIGH)

# Helper functions
def blink(pin):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)

def cleanup():
    print("Cleaning up!")
    GPIO.cleanup() # cleanup all GPIO

# Main loop
if __name__ == '__main__':
    try:
        print("Starting main loop")
        while True:
            blink(output_pin)
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        cleanup()
    except Exception as e:
        print(e)
        cleanup()
        sys.exit(1)

# If you are new to Raspberry Pi GPIO, you can find more information here.
#
# I have also created a similar tutorial on how to setup a Raspberry Pi GPIO with a 8x8 LED Matrix.
#
# Have fun!
#
# Related