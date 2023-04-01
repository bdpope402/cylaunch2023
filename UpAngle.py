import board, adafruit_bno055
from math import *
from time import sleep
import move

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_bno055.BNO055_I2C(i2c)

error = 9999


def AngleToUp():
    averageroll = 0
    for x in range(3):
        ax, ay, az = sensor.acceleration

        aMag = sqrt(ax**2 + ay**2 + az**2)
        if aMag >= 100:
            log.writeTo(f"ERROR, Acceleration Magnitude from UpAngle: {aMag}")
            return error
        roll = degrees(atan2(ay, az))

        if roll < 0:
            roll += 360

        averageroll += roll

        sleep(0.05)

    return averageroll / 3


while True:
    rAng = AngleToUp()
    print(f"Roll: {rAng}")
    turn = round((rAng / 3.8), 0)
    print(f"Turn: {turn}")
    if turn > 0:
        move.move.spinF(1)
    elif turn < 0:
        move.move.spinB(1)
    else:
        print("Nah")
    sleep(0.1)

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
