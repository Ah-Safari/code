from gpiozero import LED
from signal import pause
from time import sleep
    
led1=LED(17)
led2=LED(18)
led3=LED(27)
while True:
    led1.blink(1,1)
    led2.blink(1,2)
    led3.blink(1,3)
    sleep(1)
    led1.blink(1,1)
    led2.blink(1,2)
    led3.blink(1,3)
    pause()
    

    

