import board, adafruit_bno055
import RPi.GPIO as GPIO
from time import sleep
from math import *

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_bno055.BNO055_I2C(i2c)

def checkIfLaunching():

    accelerationX, accelerationY, accelerationZ = sensor.acceleration
    accelerationMag = sqrt(accelerationX**2 + accelerationY**2 + accelerationZ**2)

    print("Acceleration Magnitude: " + str(accelerationMag))
    if(accelerationMag < 20):
        return False
    else:
        return True
    
def checkIfLanded():
    accelerationX, accelerationY, accelerationZ = sensor.acceleration
    accelerationMag = sqrt(accelerationX**2 + accelerationY**2 + accelerationZ**2)

    print("Acceleration Magnitude: " + str(accelerationMag))
    if(accelerationMag > 9.78 and accelerationMag < 9.81 ):
        return True
    else:
        return False
