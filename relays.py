import RPi.GPIO as GPIO

# Setup the Power Relay Pin
pRelayPin = 5  # This is BCM 5, Wiring 21, Onboard 25

# Setup the Motor Relay Pins
motorA0 = 6
motorA1 = 13
motorB0 = 19
motorB1 = 26

power = False
downA = True
downB = True

# Set Output Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)
GPIO.setup(motorA0, GPIO.OUT)
GPIO.setup(motorA1, GPIO.OUT)
GPIO.setup(motorB0, GPIO.OUT)
GPIO.setup(motorB1, GPIO.OUT)

def powerOn():
    print("Motors Power On")
    power = True
    GPIO.output(pRelayPin, GPIO.HIGH)

def powerOff():
    print("Motors Power On")
    power = False
    GPIO.output(pRelayPin, GPIO.LOW)

def motorA_Up():
    print("Motor A Up")
    if (power & downA):
        powerOff()
        downA = False
        GPIO.output(motorA0, GPIO.HIGH)
        GPIO.output(motorA1, GPIO.HIGH)
        powerOn()
    else:
        GPIO.output(motorA0, GPIO.HIGH)
        GPIO.output(motorA1, GPIO.HIGH)
        powerOn()

def motorB_Up():
    print("Motor B Up")
    if power & downB:
        powerOff()
        GPIO.output(motorB0, GPIO.HIGH)
        GPIO.output(motorB1, GPIO.HIGH)
        powerOn()
    else:
        GPIO.output(motorB0, GPIO.HIGH)
        GPIO.output(motorB1, GPIO.HIGH)
        powerOn()

def motorA_Down():
    print("Motor A Down")
    if power & (!down):
        powerOff()
        GPIO.output(motorA0, GPIO.LOW)
        GPIO.output(motorA1, GPIO.LOW)

def motorB_Down():
    print("Motor B Down")
    GPIO.output(motorB0, GPIO.LOW)
    GPIO.output(motorB1, GPIO.LOW)

def dualMotor_Up():
    print("Dual Motor Up")
    motorA_Up()
    motorB_Up()

def dualMotor_Down():
    print("Dual Motor Up")
    motorA_Down()
    motorB_Down()