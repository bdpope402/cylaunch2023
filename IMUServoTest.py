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


servo1PIN = 21
servo2PIN = 16
frequency = 50
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo1PIN, GPIO.OUT)
GPIO.setup(servo2PIN, GPIO.OUT)

pwm1 = GPIO.PWM(servo1PIN, frequency)  # GPIO servoPIN for PWM with 50Hz
pwm2 = GPIO.PWM(servo2PIN, frequency)  # GPIO servoPIN for PWM with 50Hz

pwm1.start(0)  # Initialization servo 1
pwm2.start(0)  # Initialization servo 2


while True:
    accelerationX, accelerationY, accelerationZ = sensor.acceleration
    gravityX, gravityY, gravityZ = sensor.gravity
    accelerationMag = sqrt(accelerationX**2 + accelerationY**2 + accelerationZ**2)
    gravityMag = sqrt(gravityX**2 + gravityY**2 + gravityZ**2)
    print(f"Acceleration X: {accelerationX}")
    print(f"Acceleration Y: {accelerationY}")
    print(f"Acceleration Z: {accelerationZ}")
    print(f"Gravity X: {gravityX}")
    print(f"Gravity Y: {gravityY}")
    print(f"Gravity Z: {gravityZ}")
    print(f"Acceleration Magnitude: {accelerationMag}")
    print(f"Gravity Magnitude: {gravityMag}")

    # desiredAngle = float(input("Angle: "))
    # servo = float(input("Servo: "))

    if gravityX >= 0:
        desiredAngle = 0
    else:
        desiredAngle = 270
    servo = 1

    if desiredAngle < 0 or desiredAngle > 270:
        pwm1.stop()
        pwm2.stop()
        GPIO.cleanup()
        print("break")
        break
    else:
        if servo == 1:
            pwm1.ChangeDutyCycle(angle2DutyCycle(desiredAngle))
        elif servo == 2:
            pwm2.ChangeDutyCycle(angle2DutyCycle(desiredAngle))
        else:
            pwm1.stop()
            pwm2.stop()
            GPIO.cleanup()
            print("break")
            break
    sleep(.1)
