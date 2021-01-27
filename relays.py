import RPi.GPIO as GPIO

# Setup the Power Relay Pin
pRelayPin = 5  # This is BCM 5, Wiring 21, Onboard 25

# Setup the Motor Relay Pins
MA0 = 6
MA1 = 13
MB0 = 19
MB1 = 26
global pwr, dir_a, dir_b
pwr = False
dir_a = True
dir_b = True
# Set Output Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(pRelayPin, GPIO.OUT)
GPIO.setup(MA0, GPIO.OUT)
GPIO.setup(MA1, GPIO.OUT)
GPIO.setup(MB0, GPIO.OUT)
GPIO.setup(MB1, GPIO.OUT)


def setup_globals():
    global pwr, dir_a, dir_b
    pwr = False
    dir_a = True
    dir_b = True


# Primary control Method
def motor_control(motor_a, motor_b, down):
    if motor_a and motor_b:
        if down:
            dual_motor_down()
        else:
            dual_motor_up()
    elif motor_a:
        if down:
            motor_a_down()
        else:
            motor_a_down()
    elif motor_b:
        if down:
            motor_b_down()
        else:
            motor_b_up()


def power_on():
    print("Motors Power On")
    global pwr
    pwr = True
    GPIO.output(pRelayPin, GPIO.HIGH)


def power_off():
    print("Motors Power On")
    global pwr
    pwr = False
    GPIO.output(pRelayPin, GPIO.LOW)


def motor_a_up():
    print("Motor A Up")
    if pwr and dir_a:
        power_off()
        GPIO.output(MA0, GPIO.HIGH)
        GPIO.output(MA1, GPIO.HIGH)
        power_on()
        global dir_a
        dir_a = False
    else:
        GPIO.output(MA0, GPIO.HIGH)
        GPIO.output(MA1, GPIO.HIGH)
        power_on()


def motor_b_up():
    print("Motor B Up")
    if pwr and dir_b:
        power_off()
        GPIO.output(MB0, GPIO.HIGH)
        GPIO.output(MB1, GPIO.HIGH)
        power_on()
        global dir_b
        dir_b = False
    else:
        GPIO.output(MB0, GPIO.HIGH)
        GPIO.output(MB1, GPIO.HIGH)
        power_on()


def motor_a_down():
    print("Motor A Down")
    if pwr and not dir_a:
        power_off()
        GPIO.output(MA0, GPIO.LOW)
        GPIO.output(MA1, GPIO.LOW)
        power_on()
        global dir_a
        dir_a = True
    else:
        GPIO.output(MA0, GPIO.LOW)
        GPIO.output(MA1, GPIO.LOW)
        power_on()


def motor_b_down():
    print("Motor B Down")
    if pwr and not dir_b:
        power_off()
        GPIO.output(MB0, GPIO.LOW)
        GPIO.output(MB1, GPIO.LOW)
        power_on()
        global dir_b
        dir_b = True
    else:
        GPIO.output(MB0, GPIO.LOW)
        GPIO.output(MB1, GPIO.LOW)
        power_on()


def dual_motor_up():
    print("Dual Motor Up")
    motor_a_up()
    motor_b_up()


def dual_motor_down():
    print("Dual Motor Up")
    motor_a_down()
    motor_b_down()
