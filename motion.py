from gpiozero import LED
from gpiozero import MotionSensor
from signal import pause

led_motion=LED(17)
led_no_motion=LED(18)
pir=MotionSensor(4)
led_motion.off()
led_no_motion.off()

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    led_motion.on()
    led_no_motion.off()
    pir.wait_for_no_motion()
    led_no_motion.on()
    led_motion.off()
    print("Motion not detected")

pause()