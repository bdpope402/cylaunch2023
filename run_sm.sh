#!/usr/bin/bash
FILE=/home/cylaunch/payload_code/flags/SMRestart.cyl
if [[ -f "$FILE" ]]; then
    /usr/bin/python3 /home/cylaunch/payload_code/launch_sm.py
fi
# /usr/bin/python3 /home/cylaunch/payload_code/launch_sm.py &