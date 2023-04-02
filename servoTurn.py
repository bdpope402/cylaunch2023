import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)   
servo1PIN = 20
frequency = 50
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo1PIN, GPIO.OUT)

global pwm1
global pwm2
pwm1 = GPIO.PWM(servo1PIN, frequency) # GPIO servoPIN for PWM with 50Hz
# print("Start")
pwm1.start(0) # Initialization servo 1

def angle2DutyCycle(angle):
    dutyCycle = (angle / 27) + 2.5
    print(f"Angle = {angle}")
    print(f"Duty Cycle = {dutyCycle}")
    return dutyCycle

def moveServo(degrees):
    if(degrees < 0 or degrees > 270):
        pwm1.stop()
        GPIO.cleanup()
        return -1
    else:
        pwm1.ChangeDutyCycle(angle2DutyCycle(degrees))
        sleep(2)
        return 0
        # else:
        #     pwm1.stop()
        #     pwm2.stop()
        #     GPIO.cleanup()
        #     return -1
