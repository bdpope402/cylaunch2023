from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

# Stepper 1 is body rotation motor, 1.8° per step, 3.6° per doublestep
# Stepper 2 is linear actuator, .0018 mm per step, .0038 mm per doublestep


class move:

    def __init__(self):
        self.kit = MotorKit()
    def spinF(self, angle):
        steps = move.convertAngle(angle)
        i = 0
        while i < steps:
            self.kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            i += 1
        # self.kit.stepper1.release()
    
    def spinF_norelease(self, angle):
        steps = move.convertAngle(angle)
        i = 0
        while i < steps:
            self.kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            i += 1
        #kit.stepper1.release()

    def spinB(self, angle):
        steps = move.convertAngle(angle)
        i = 0
        while i < steps:
            self.kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            i += 1
        # kit.stepper1.release()

    def extendF(self, steps):
        i = 0
        while i < steps:
            self.kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            i += 1
        # kit.stepper2.release()

    def extendB(self, steps):
        i = 0
        while i < steps:
            self.kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            i += 1
        #kit.stepper2.release()

    def convertAngle(angle):
        return angle / 3.6
    
    def releaseLin(self):
        self.kit.stepper2.release()

    def releaseStepper(self):
        self.kit.stepper1.release()


# move.spinF(200)
