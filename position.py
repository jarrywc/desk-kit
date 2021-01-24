import RPi.GPIO as GPIO
import board
import busio
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
# Setup the Potentiometer (this should already be in the desk actuators)
ads = ADS.ADS1115(i2c)
chanLeftA = AnalogIn(ads, ADS.P0)
chanLeftB = AnalogIn(ads, ADS.P1)
chanRightA = AnalogIn(ads, ADS.P2)
chanRightB = AnalogIn(ads, ADS.P3)