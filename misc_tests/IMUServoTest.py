import board, adafruit_bno055
import RPi.GPIO as GPIO
from time import sleep
from math import *

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_bno055.BNO055_I2C(i2c)

GPIO.setwarnings(False)


def angle2DutyCycle(angle):
    dutyCycle = (angle / 27) + 2.5
    print(f"Angle = {angle}")
    print(f"Duty Cycle = {dutyCycle}")
    return dutyCycle


servoPIN = 19
frequency = 50
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

pwm = GPIO.PWM(servoPIN, frequency)  # GPIO servoPIN for PWM with 50Hz

pwm.start(0)  # Initialization servo

lastDAng = None

while True:
    desiredAngle = float(input("Angle: "))

    if desiredAngle != lastDAng:
        print(f"Desired: {desiredAngle}°")
        if desiredAngle < 0 or desiredAngle > 270:
            pwm.stop()
            GPIO.cleanup()
            print("Out of range")
            break
        else:
            pwm.ChangeDutyCycle(angle2DutyCycle(desiredAngle))

    lastDAng = desiredAngle
    sleep(1)
