import board, adafruit_bno055
import RPi.GPIO as GPIO
from time import sleep
from math import sqrt
from cyllogger import cyllogger

log = cyllogger("RocketCheck")

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_bno055.BNO055_I2C(i2c)


def checkIfLaunching():
    averageAcceleration = 0
    for x in range(3):
        accelerationX, accelerationY, accelerationZ = sensor.acceleration
        accelerationMag = sqrt(
            accelerationX**2 + accelerationY**2 + accelerationZ**2
        )
        if accelerationMag >= 100:
            log.writeTo(f"ERROR, Acceleration Magnitude: {accelerationMag}")
            # print(f"ERROR, Acceleration Magnitude: {averageAcceleration}")
            return False
        averageAcceleration += accelerationMag
        sleep(0.05)

    averageAcceleration = averageAcceleration / 3

    if averageAcceleration < 20:
        log.writeTo(f"Not Launched, Acceleration Magnitude: {averageAcceleration}")
        # print(f"Not Launched, Acceleration Magnitude: {averageAcceleration}")
        return False
    else:
        log.writeTo(f"Launched, Acceleration Magnitude: {averageAcceleration}")
        # print(f"Launched, Acceleration Magnitude: {averageAcceleration}")
        return True


def checkIfLanded():
    averageAcceleration = 0
    for x in range(3):
        accelerationX, accelerationY, accelerationZ = sensor.acceleration
        accelerationMag = sqrt(
            accelerationX**2 + accelerationY**2 + accelerationZ**2
        )
        if accelerationMag >= 100:
            log.writeTo(f"ERROR, Acceleration Magnitude: {accelerationMag}")
            # print(f"ERROR, Acceleration Magnitude: {averageAcceleration}")
            return False
        averageAcceleration += accelerationMag
        sleep(0.05)

    averageAcceleration = averageAcceleration / 3

    if averageAcceleration < 10:
        log.writeTo(f"Landed, Acceleration Magnitude: {averageAcceleration}")
        # print(f"Landed, Acceleration Magnitude: {averageAcceleration}")
        return True
    else:
        log.writeTo(f"Not Landed, Acceleration Magnitude: {averageAcceleration}")
        # print(f"Not Landed, Acceleration Magnitude: {averageAcceleration}")
        return False
