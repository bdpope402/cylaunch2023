import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

servoPIN = 21
alogPos = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
#GPIO.setup(alogPos, GPIO.IN) # Servo outputs analog signal for feedback, not even sure if thats useful for us

pwm = GPIO.PWM(servoPIN, 50) # GPIO servoPIN for PWM with 50Hz
print("2.5 (0)")
pwm.start(2.5) # Initialization
sleep(3)

def Angle(Ang):
    Cycle = (Ang / 27) + 2.5
    print(f"Angle = {Ang}")
    print(f"Duty = {Cycle}")
    return Cycle

pwm.ChangeDutyCycle(Angle(10))
sleep(3)
pwm.ChangeDutyCycle(Angle(180))
sleep(3)
pwm.ChangeDutyCycle(Angle(200))
sleep(3)

"""
pwm.ChangeDutyCycle(7.5)
print("7.5 (135)")
sleep(3)
pwm.ChangeDutyCycle(12.5)
print("12.5 (270)")
sleep(3)
pwm.ChangeDutyCycle(7.5)
print("7.5 (135)")
sleep(3)
pwm.ChangeDutyCycle(2.5)
print("2.5 (0)")
sleep(3)
pwm.ChangeDutyCycle(7.5)
print("7.5 (135)")
sleep(3)
"""

pwm.stop()
GPIO.cleanup()
