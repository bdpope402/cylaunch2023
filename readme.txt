Welcome to the CyLaunch 2023 Codebase.

CyLaunch is Iowa State's NASA Student Launch team.

CyLaunch_SM.png is a visual interview of our state machine.

The Raspberry pi will start the launch SM upon startup when the SMRestart.cyl exists. (a cronjob calls run_sm.sh).

launch_sm is the top level function that implements CyLaunch_SM.png

Helper functions:
cyllogger
    -Logging object that writes timestamped messages to the provided file
interrupt
    - A GPIO interrupt class
move
    - An object for controlling our stepper motors
photo_editor
    - An object that can add filters and timestamps to photos
RocketCheck
    - Checks if the rocket is launched or not based on Magnitude of acceleration
servoTurn
    - An object to turn the servos
stopstep
    - releases all stepper motors immediately
UpAngle
    - Calculates the angle of the door closest to "up"