import RPi.GPIO as GPIO
from time import sleep
class servoTurn:
    def __init__(self):       
        GPIO.setwarnings(False)   
        servo1PIN = 19
        frequency = 50
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo1PIN, GPIO.OUT)
        self.pwm1 = GPIO.PWM(servo1PIN, frequency) # GPIO servoPIN for PWM with 50Hz
        # print("Start")
        self.pwm1.start(0) # Initialization servo 1

    def moveServo(self,degrees):
        if(degrees < 0 or degrees > 270):
            self.pwm1.stop()
            GPIO.cleanup()
            return -1
        else:
            self.pwm1.ChangeDutyCycle(angle2DutyCycle(degrees))
            sleep(2)
            return 0

def angle2DutyCycle(angle):
    dutyCycle = (angle / 27) + 2.5
    print(f"Angle = {angle}")
    print(f"Duty Cycle = {dutyCycle}")
    return dutyCycle
