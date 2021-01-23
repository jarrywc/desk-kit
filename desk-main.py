import RPi.GPIO as GPIO
import board
import busio
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
# Setup the Potentiameter (this should already be in the desk actuators)
ads = ADS.ADS1115(i2c)
chanLeftA = AnalogIn(ads, ADS.P0)
chanLeftB = AnalogIn(ads, ADS.P1)
chanRightA = AnalogIn(ads, ADS.P2)
chanRightB = AnalogIn(ads, ADS.P3)
# Setup the Relay Pin
relayPin = 5  # This is BCM 5, Wiring 21, Onboard 25
# Setup the Motor Controller Pins
motorA0 = 6
motorA1 = 13
motorB0 = 19
motorB1 = 26
# Set Output Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)
GPIO.setup(motorA0, GPIO.OUT)
GPIO.setup(motorA1, GPIO.OUT)
GPIO.setup(motorB0, GPIO.OUT)
GPIO.setup(motorB1, GPIO.OUT)


def systemOn():
    GPIO.output(relayPin, GPIO.HIGH)
    print("System On")


def systemOff():
    GPIO.output(relayPin, GPIO.LOW)
    print("System Off")


def motorOff():
    print("Motors Off")
    GPIO.output(motorA0, GPIO.LOW)
    GPIO.output(motorA1, GPIO.LOW)
    GPIO.output(motorB0, GPIO.LOW)
    GPIO.output(motorB1, GPIO.LOW)


def directA():
    print("Direction A")
    GPIO.output(motorA0, GPIO.HIGH)
    GPIO.output(motorA1, GPIO.LOW)
    GPIO.output(motorB0, GPIO.HIGH)
    GPIO.output(motorB1, GPIO.LOW)


def directB():
    print("Direction B")
    GPIO.output(motorA0, GPIO.LOW)
    GPIO.output(motorA1, GPIO.HIGH)
    GPIO.output(motorB0, GPIO.LOW)
    GPIO.output(motorB1, GPIO.HIGH)


def printI2C():
    print("CL0 ", chanLeftA.value, chanLeftA.voltage)
    print("CL1 ", chanLeftB.value, chanLeftB.voltage)
    print("CL2 ", chanRightA.value, chanRightA.voltage)
    print("CL3 ", chanRightB.value, chanRightB.voltage)


def main():
    printI2C()
    motorOff()
    time.sleep(2)
    systemOn()
    time.sleep(2)
    directA()
    time.sleep(6)
    motorOff()
    systemOff()
    time.sleep(6)
    systemOn()
    directB()
    time.sleep(6)
    motorOff()
    systemOff()


if __name__ == '__main__':
    main()
