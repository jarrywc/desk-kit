import RPi.GPIO as GPIO

# Setup the Power Relay Pin
pRelayPin = 5  # This is BCM 5, Wiring 21, Onboard 25

# Setup the Motor Relay Pins
motorA0 = 6
motorA1 = 13
motorB0 = 19
motorB1 = 26
# Status Booleans
power = False
dirA_D = True
dirB_D = True

# Set Output Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(pRelayPin, GPIO.OUT)
GPIO.setup(motorA0, GPIO.OUT)
GPIO.setup(motorA1, GPIO.OUT)
GPIO.setup(motorB0, GPIO.OUT)
GPIO.setup(motorB1, GPIO.OUT)

# Primary control Method
def motorControl(motorA, motorB, down):
    if motorA and motorB:
        if down:
            dualMotor_Down()
        else:
            dualMotor_Up()
    elif motorA:
        if down:
            motorA_Down()
        else:
            motorA_Up()
    elif motorB:
        if down:
            motorB_Down()
        else:
            motorB_Up()


def powerOn():
    print("Motors Power On")
    global power
    power = True
    GPIO.output(pRelayPin, GPIO.HIGH)


def powerOff():
    print("Motors Power On")
    global power
    power = False
    GPIO.output(pRelayPin, GPIO.LOW)


def motorA_Up():
    print("Motor A Up")
    if power and dirA_D:
        powerOff()
        GPIO.output(motorA0, GPIO.HIGH)
        GPIO.output(motorA1, GPIO.HIGH)
        powerOn()
        global dirA_D
        dirA_D = False
    else:
        GPIO.output(motorA0, GPIO.HIGH)
        GPIO.output(motorA1, GPIO.HIGH)
        powerOn()


def motorB_Up():
    print("Motor B Up")
    if power and dirB_D:
        powerOff()
        GPIO.output(motorB0, GPIO.HIGH)
        GPIO.output(motorB1, GPIO.HIGH)
        powerOn()
        global dirB_D
        dirB_D = False
    else:
        GPIO.output(motorB0, GPIO.HIGH)
        GPIO.output(motorB1, GPIO.HIGH)
        powerOn()


def motorA_Down():
    print("Motor A Down")
    if power and not dirA_D:
        powerOff()
        GPIO.output(motorA0, GPIO.LOW)
        GPIO.output(motorA1, GPIO.LOW)
        powerOn()
        global dirA_D
        dirA_D = True
    else:
        GPIO.output(motorA0, GPIO.LOW)
        GPIO.output(motorA1, GPIO.LOW)
        powerOn()


def motorB_Down():
    print("Motor B Down")
    if power and not dirB_D:
        powerOff()
        GPIO.output(motorB0, GPIO.LOW)
        GPIO.output(motorB1, GPIO.LOW)
        powerOn()
        global dirB_D
        dirB_D = True
    else:
        GPIO.output(motorB0, GPIO.LOW)
        GPIO.output(motorB1, GPIO.LOW)
        powerOn()


def dualMotor_Up():
    print("Dual Motor Up")
    motorA_Up()
    motorB_Up()


def dualMotor_Down():
    print("Dual Motor Up")
    motorA_Down()
    motorB_Down()
