import RPi.GPIO as GPIO
from time import sleep

running = True

GPIO.setwarnings(False)

def Angle(Ang):
    Cycle = (Ang / 27) + 2.5
    print(f"Angle = {Ang}")
    print(f"Duty = {Cycle}")
    return Cycle

servoPIN = 21
alogPos = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
#GPIO.setup(alogPos, GPIO.IN) # Servo outputs analog signal for feedback, not even sure if thats useful for us

pwm = GPIO.PWM(servoPIN, 50) # GPIO servoPIN for PWM with 50Hz
print("Start")
pwm.start(0) # Initialization

while running:
    deg = float(input("Angle: "))
    if deg < 0 or deg > 270:
        running = False
        pwm.stop()
        GPIO.cleanup()
        break
    else:
        pwm.ChangeDutyCycle(Angle(deg))
        #sleep(.5)
