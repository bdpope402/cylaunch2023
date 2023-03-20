import RPi.GPIO as GPIO
from time import sleep



def angle2DutyCycle(angle):
    dutyCycle = (angle / 27) + 2.5
    print(f"Angle = {angle}")
    print(f"Duty Cycle = {dutyCycle}")
    return dutyCycle

def moveServo(servo_num, degrees):
    GPIO.setwarnings(False)
    servo1PIN = 21
    servo2PIN = 16
    frequency = 50
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo1PIN, GPIO.OUT)
    GPIO.setup(servo2PIN, GPIO.OUT)

    pwm1 = GPIO.PWM(servo1PIN, frequency) # GPIO servoPIN for PWM with 50Hz
    pwm2 = GPIO.PWM(servo2PIN, frequency) # GPIO servoPIN for PWM with 50Hz
    # print("Start")
    pwm1.start(0) # Initialization servo 1
    pwm2.start(0) # Initialization servo 2

    if degrees < 0 or degrees > 270:
        pwm1.stop()
        pwm2.stop()
        GPIO.cleanup()
        return -1
    else:
        if servo_num == 1:
            pwm1.ChangeDutyCycle(angle2DutyCycle(degrees))
            return 0
        elif servo_num == 2:
            pwm2.ChangeDutyCycle(angle2DutyCycle(degrees))
            return 0
        else:
            pwm1.stop()
            pwm2.stop()
            GPIO.cleanup()
            return -1
