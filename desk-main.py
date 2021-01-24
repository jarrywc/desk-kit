import RPi.GPIO as GPIO
import board
import busio
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

from relays import motorControl

from position import printI2C

def slp(amt):
    time.sleep(amt)

def main():
    printI2C()
    slp(2)
    motorControl(True, True, True)


if __name__ == '__main__':
    main()
