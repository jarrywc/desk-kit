import RPi.GPIO as GPIO
import board
import busio
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import relay_h


# Hall Sensor
hall_A0 = 22
hall_A1 = 27
hall_B0 = 24
hall_B1 = 23

# Setup the Power Relay Pin
pRelayPin = 5  # This is BCM 5, Wiring 21, Onboard 25

# Setup the Motor Relay Pins
MA0 = 6     # Right side, White Connector
MA1 = 13    # Right side, White Connector
MB0 = 19    # Left side, Yellow Connector
MB1 = 26    # Left side, Yellow Connector


def sleeper(duration):
    duration = duration/30
    for x in range(1, 30):
        time.sleep(duration)
        #position.printI2C()


# Primary control Method
def motor_control(motor_a, motor_b, down, duration):
    # Set Output Pins
    GPIO.setup(pRelayPin, GPIO.OUT)
    GPIO.setup(MA0, GPIO.OUT)
    GPIO.setup(MA1, GPIO.OUT)
    GPIO.setup(MB0, GPIO.OUT)
    GPIO.setup(MB1, GPIO.OUT)


    print("Motors Power On for " + str(duration) + " seconds")
    if motor_a and motor_b:
        if down:
            set_mb(False)
            set_ma(False)
        else:
            set_mb(True)
            set_ma(True)
    elif motor_a:
        if down:
            set_ma(False)
        else:
            set_ma(True)
    elif motor_b:
        if down:
            set_mb(False)
        else:
            set_ma(True)
    GPIO.output(pRelayPin, GPIO.HIGH)
    #position.sleep_writer(duration)
    print("Motors Power Off")
    GPIO.output(pRelayPin, GPIO.LOW)
    GPIO.cleanup()


def power_off():
    print("Motors Power Off")
    GPIO.output(pRelayPin, GPIO.LOW)


def set_ma(value):
    power_off()
    if value is True:
        print("Motor A Up")
        GPIO.output(MA0, GPIO.HIGH)
        GPIO.output(MA1, GPIO.HIGH)
    else:
        print("Motor A Down")
        GPIO.output(MA0, GPIO.LOW)
        GPIO.output(MA1, GPIO.LOW)


def set_mb(value):
    power_off()
    if value is True:
        print("Motor B Up")
        GPIO.output(MB0, GPIO.HIGH)
        GPIO.output(MB1, GPIO.HIGH)
    else:
        print("Motor B Down")
        GPIO.output(MB0, GPIO.LOW)
        GPIO.output(MB1, GPIO.LOW)

def slp(amt):
    time.sleep(amt)


def prompt():
    prompt = float(input("Input value "))
    if prompt > 0:
        relay_h.motor_control(True, False, True, prompt)
    elif prompt < 0:
        prompt = prompt * (-1)
        relay_h.motor_control(False, True, False, prompt)


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(hall_A0, GPIO.IN)
    GPIO.setup(hall_A1, GPIO.IN)
    GPIO.setup(hall_B0, GPIO.IN)
    GPIO.setup(hall_B1, GPIO.IN)
    try:
        while True:
            prompt()
            if not GPIO.input(hall_A0):
                print("A0 On")
            if not GPIO.input(hall_A1):
                print("A1 On")
            if not GPIO.input(hall_B0):
                print("B0 On")
            if not GPIO.input(hall_B1):
                print("B1 On")


    except KeyboardInterrupt:
        power_off()
        GPIO.cleanup()


if __name__ == '__main__':
    main()
