import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
sleepTime=.1
 
lightpin=18
buttonpin=17

GPIO.setup(lightpin,GPIO.OUT)
GPIO.setup(buttonpin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.output(lightpin, False)

try:
    while True:
        GPIO.output(lightpin,not GPIO.input(buttonpin))
        sleep(.1)
finally:
    GPIO.output(lightpin, False)
    GPIO.cleanup()