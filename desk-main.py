import RPi.GPIO as GPIO
import board
import busio
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import relay

def slp(amt):
    time.sleep(amt)


def prompt():
    prompt = float(input("Input value "))
    if prompt > 0:
        relay.motor_control(True, True, True, prompt)
    elif prompt < 0:
        prompt = prompt*(-1)
        relay.motor_control(True, True, False, prompt)


def main():

    try:
        while True:
            prompt()

    except KeyboardInterrupt:
        relay.power_off()
        GPIO.cleanup()


if __name__ == '__main__':
    main()
