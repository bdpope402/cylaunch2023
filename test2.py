import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

def angle2DutyCycle(angle):
    dutyCycle = (angle / 27) + 2.5
    print(f"Angle = {angle}")
    print(f"Duty Cycle = {dutyCycle}")
    return dutyCycle

servo1PIN = 19
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

while True:
    desiredAngle = float(input("Angle: "))
    servo = float(input("Servo: "))
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
