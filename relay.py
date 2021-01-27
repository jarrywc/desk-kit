import RPi.GPIO as GPIO
import time
import position

# Setup the Power Relay Pin
pRelayPin = 5  # This is BCM 5, Wiring 21, Onboard 25

# Setup the Motor Relay Pins
MA0 = 6
MA1 = 13
MB0 = 19
MB1 = 26

def sleeper(duration):
    duration = duration/10
    for x in range(1,10):
        time.sleep(duration)
        position.printI2C()


# Primary control Method
def motor_control(motor_a, motor_b, down, duration):
    # Set Output Pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pRelayPin, GPIO.OUT)
    GPIO.setup(MA0, GPIO.OUT)
    GPIO.setup(MA1, GPIO.OUT)
    GPIO.setup(MB0, GPIO.OUT)
    GPIO.setup(MB1, GPIO.OUT)

    pwr = False
    dir_a = True
    dir_b = True
    print("Motors Power On for " + str(duration) + " seconds")
    if motor_a and motor_b:
        if down:
            print("Motor A Down")
            if pwr and not dir_a:
                power_off()
                GPIO.output(MA0, GPIO.LOW)
                GPIO.output(MA1, GPIO.LOW)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
                dir_a = True
            else:
                GPIO.output(MA0, GPIO.LOW)
                GPIO.output(MA1, GPIO.LOW)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
            print("Motor B Down")
            if pwr and not dir_b:
                power_off()
                GPIO.output(MB0, GPIO.LOW)
                GPIO.output(MB1, GPIO.LOW)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
                dir_b = True
            else:
                GPIO.output(MB0, GPIO.LOW)
                GPIO.output(MB1, GPIO.LOW)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
        else:
            print("Motor A Up")
            if pwr and dir_a:
                power_off()
                GPIO.output(MA0, GPIO.HIGH)
                GPIO.output(MA1, GPIO.HIGH)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
                dir_a = False
            else:
                GPIO.output(MA0, GPIO.HIGH)
                GPIO.output(MA1, GPIO.HIGH)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
            print("Motor B Up")
            if pwr and dir_b:
                power_off()
                GPIO.output(MB0, GPIO.HIGH)
                GPIO.output(MB1, GPIO.HIGH)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
                dir_b = False
            else:
                GPIO.output(MB0, GPIO.HIGH)
                GPIO.output(MB1, GPIO.HIGH)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
    elif motor_a:
        if down:
            print("Motor A Down")
            if pwr and not dir_a:
                power_off()
                GPIO.output(MA0, GPIO.LOW)
                GPIO.output(MA1, GPIO.LOW)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
                dir_a = True
            else:
                GPIO.output(MA0, GPIO.LOW)
                GPIO.output(MA1, GPIO.LOW)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
        else:
            print("Motor A Up")
            if pwr and dir_a:
                power_off()
                GPIO.output(MA0, GPIO.HIGH)
                GPIO.output(MA1, GPIO.HIGH)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
                dir_a = False
            else:
                GPIO.output(MA0, GPIO.HIGH)
                GPIO.output(MA1, GPIO.HIGH)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
    elif motor_b:
        if down:
            print("Motor B Down")
            if pwr and not dir_b:
                power_off()
                GPIO.output(MB0, GPIO.LOW)
                GPIO.output(MB1, GPIO.LOW)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
                dir_b = True
            else:
                GPIO.output(MB0, GPIO.LOW)
                GPIO.output(MB1, GPIO.LOW)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
        else:
            print("Motor B Up")
            if pwr and dir_b:
                power_off()
                GPIO.output(MB0, GPIO.HIGH)
                GPIO.output(MB1, GPIO.HIGH)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
                dir_b = False
            else:
                GPIO.output(MB0, GPIO.HIGH)
                GPIO.output(MB1, GPIO.HIGH)
                pwr = True
                GPIO.output(pRelayPin, GPIO.HIGH)
    sleeper(duration)
    print("Motors Power Off")
    GPIO.output(pRelayPin, GPIO.LOW)
    GPIO.cleanup()

def power_off():
    print("Motors Power On")
    GPIO.output(pRelayPin, GPIO.LOW)