#----------------------------------------------------
# Interrupts to help with payload positioning
#----------------------------------------------------
import signal                   
import sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

BUTTON_GPIO = 20

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_callback(channel):
    if not GPIO.input(BUTTON_GPIO):
        print("Button pressed!")
    else:
        print("Button released!")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, 
            callback=button_callback, bouncetime=100)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
