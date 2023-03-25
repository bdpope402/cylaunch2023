from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit = MotorKit()
i=0
j=0
while(i < 400):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE )
    kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE )

    i = i + 1

# while(j < 100):
#     kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE )
#     j = j + 1

while(i > 0):
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE )
    i = i - 1

kit.stepper1.release()
kit.stepper2.release()