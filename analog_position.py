import RPi.GPIO as GPIO
import csv
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


def printI2C():
    print("CL0 ", chanLeftA.value, chanLeftA.voltage)
    print("CL1 ", chanLeftB.value, chanLeftB.voltage)
    print("CL2 ", chanRightA.value, chanRightA.voltage)
    print("CL3 ", chanRightB.value, chanRightB.voltage)


def return_i2c():
    return str(
        str(chanLeftA.value) + "," + str(chanLeftB.value) + "," + str(chanRightA.value) + "," + str(
            chanRightB.value) + "," + str(chanLeftA.voltage) + "," + str(chanLeftB.voltage) + "," + str(
            chanRightA.voltage) + "," + str(chanRightB.voltage))


def sleep_writer(duration):
    duration = duration / 100
    with open('position_val.csv', mode='w') as position_file:
        value_writer = csv.writer(position_file)
        for x in range(1, 100):
            time.sleep(duration)

            #value_writer.writerow(
            #    ["Left Val A", "Left Val B", "Right Val A", "Right Val B",
            #     "Left Vol A", "Left Vol B", "Right Vol A", "Right Vol B"])
            value_writer.writerow(
                [str(chanLeftA.value), str(chanLeftB.value), str(chanRightA.value), str(chanRightB.value),
                 str(chanLeftA.voltage), str(chanLeftB.voltage), str(chanRightA.voltage), str(chanRightB.voltage)])
