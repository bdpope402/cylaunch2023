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


"""
while True:
    print(f"Angle to up: {AngleToUp()}")
"""

"""
while True:
    rAng = AngleToUp()
    print(f"Roll: {rAng}")
    turn = int(rAng / 3.8)
    print(f"Turn Steps: {turn}")
    # if rAng > 180:
    #     move.move.spinB(5)
    # elif rAng <= 180:
    #     move.move.spinF(5)
    # else:
    #     print("Nah")
    # sleep(0.05)
"""

"""
while True:
    ax, ay, az = sensor.acceleration
    # print(f"ax {ax}, ay {ay}, az {az}")

    # Compute roll, pitch, and yaw (Euler angles) from acceleration readings
    roll = degrees(atan2(ay, az))
    pitch = degrees(atan2(-ax, sqrt(ay**2 + az**2)))

    if roll < 0:
        roll += 360

    if pitch < 0:
        pitch += 360

    # Print the Euler angles in degrees
    print("Roll: {:.2f} degrees".format(roll))
    print("Pitch: {:.2f} degrees".format(pitch))

    sleep(0.05)
"""
