from adafruit_motorkit import MotorKit
from adafruit_motor import stepper


class move:
    def spinF(steps):
        kit = MotorKit()
        i = 0
        while i < steps:
            kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            i += 1
        kit.stepper1.release()

    def spinB(steps):
        kit = MotorKit()
        i = 0
        while i < steps:
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            i += 1
        kit.stepper1.release()

    def extendF(steps):
        kit = MotorKit()
        i = 0
        while i < steps:
            kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
            i += 1
        kit.stepper2.release()

    def extendB(steps):
        kit = MotorKit()
        i = 0
        while i < steps:
            kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
            i += 1
        kit.stepper2.release()


# move.spinF(200)
