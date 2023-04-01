from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

# Stepper 1 is body rotation motor, 1.8° per step, 3.8° per doublestep
# Stepper 2 is linear actuator, .0018 mm per step, .0038 mm per doublestep

# def angle2stepRot(angle):
#    steps = angle

def do_spin():
    kit = MotorKit()
    i = 0
    j = 0
    while(i < 100):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
        i += 1
    while(i > 0):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        i += 1
    kit.stepper1.release()
    kit.stepper2.release()
# kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)

# i += 1

# while(j < 100):
#     kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE )
#     j = j + 1

# while i > 2000:
#    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#    i += -1

# while True:
#    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)


