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


def euler_from_quaternion(x, y, z, w):
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll = degrees(atan2(t0, t1))

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch = degrees(asin(t2))

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw = degrees(atan2(t3, t4))

    return roll, pitch, yaw  # in radians


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

lastDAng = None

while True:
    """
    accelerationX, accelerationY, accelerationZ = sensor.acceleration
    accelerationMag = sqrt(accelerationX**2 + accelerationY**2 + accelerationZ**2)

    gravityX, gravityY, gravityZ = sensor.gravity
    gravityMag = sqrt(gravityX**2 + gravityY**2 + gravityZ**2)

    eulerX, eulerY, eulerZ = sensor.euler
    eulerMag = sqrt(eulerX**2 + eulerY**2 + eulerZ**2)

    (
        linear_accelerationX,
        linear_accelerationY,
        linear_accelerationZ,
    ) = sensor.linear_acceleration
    linear_accelerationMag = sqrt(
        linear_accelerationX**2
        + linear_accelerationY**2
        + linear_accelerationZ**2
    )

    print(f"Acceleration X: {accelerationX}")
    print(f"Acceleration Y: {accelerationY}")
    print(f"Acceleration Z: {accelerationZ}")
    print(f"Acceleration Magnitude: {accelerationMag}")

    print(f"Gravity X: {gravityX}")
    print(f"Gravity Y: {gravityY}")
    print(f"Gravity Z: {gravityZ}")
    print(f"Gravity Magnitude: {gravityMag}")

    print(f"Euler X: {eulerX}")
    print(f"Euler Y: {eulerY}")
    print(f"Euler Z: {eulerZ}")
    print(f"Euler Magnitude: {eulerMag}")

    print(f"Lacceleration X: {linear_accelerationX}")
    print(f"Lacceleration Y: {linear_accelerationY}")
    print(f"Lacceleration Z: {linear_accelerationZ}")
    print(f"Lacceleration Magnitude: {linear_accelerationMag}")
    """

    quaternion = sensor.quaternion
    print(quaternion)

    roll, pitch, yaw = euler_from_quaternion(
        quaternion[0], quaternion[1], quaternion[2], quaternion[3]
    )
    print(f"roll {roll}, pitch {pitch}, yaw {yaw}")

    """
    roll, pitch, yaw = quat.to_euler_angles()
    rollDeg, pitchDeg, yawDEg = (
        math.degrees(roll),
        math.degrees(pitch),
        math.degrees(yaw),
    )

    angle_to_horizon = 90 - pitch_degrees

    print(
        "Pitch angle: {:.2f} degrees, Angle to horizon: {:.2f} degrees".format(
            pitch_degrees, angle_to_horizon
        )
    )
    """
    # desiredAngle = float(input("Angle: "))
    # servo = float(input("Servo: "))

    """
    if gravityX >= 0:
        desiredAngle = 0
    else:
        desiredAngle = 270
    """
    desiredAngle = 0
    servo = 1

    if desiredAngle != lastDAng:
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
    lastDAng = desiredAngle
    sleep(1)
