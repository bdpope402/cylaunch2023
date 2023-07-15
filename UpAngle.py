#----------------------------------------------------
# Calculates the closest door to "up" based on the
# zero point on our rocket
#----------------------------------------------------
import board, adafruit_bno055
from math import *
from time import sleep
import move
import interrupt
from cyllogger import cyllogger

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_bno055.BNO055_I2C(i2c)
FUDGE_FACTOR = -1 + 90
error = -1

log = cyllogger("UpAngleLog")


def AngleToUp():
    averageroll = 0
    for x in range(3):
        ax, ay, az = sensor.acceleration

        aMag = sqrt(ax**2 + ay**2 + az**2)
        if aMag >= 100:
            log.writeTo(f"ERROR, Acceleration Magnitude from UpAngle: {aMag}")
            print("aMag Error")
            return error
        roll = degrees(atan2(ay, az))

        averageroll += roll

    averageroll = averageroll / 3
    averageroll += FUDGE_FACTOR  # Fudge factor due to hot glue
    if averageroll < 0:
        averageroll += 360

        # sleep(0.01)
    return averageroll