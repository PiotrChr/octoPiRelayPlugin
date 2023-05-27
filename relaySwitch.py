import RPi.GPIO as GPIO
import argparse

# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)

def switch(state, pin_number):
    # set up the GPIO channels - one output
    GPIO.setup(pin_number, GPIO.OUT)

    if state == "on":
        GPIO.output(pin_number, GPIO.HIGH)  # this sends 3.3V to the pin
    elif state == "off":
        GPIO.output(pin_number, GPIO.LOW)  # this sends 0V to the pin turning it off
    else:
        print("Invalid state. Please enter 'on' or 'off'.")

# Argument parsing
parser = argparse.ArgumentParser(description='Turn GPIO pin on or off.')
parser.add_argument('-state', type=str, help='Enter "on" or "off".', required=True)
parser.add_argument('-pin', type=int, help='Enter GPIO pin number.', default=24)
args = parser.parse_args()

# Use the parsed arguments
switch(args.state, args.pin)