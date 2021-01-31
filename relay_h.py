import RPi.GPIO as GPIO
import time
#import position
#import export_position

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
    GPIO.setmode(GPIO.BCM)
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
