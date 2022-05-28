from gpiozero import LED
from time import sleep

K=float(input("sleep after:"))
led1=LED(18)
led2=LED(17)


while True:
    led1.toggle()
    led2.toggle()
    sleep(K)
    led1.toggle()
    led2.toggle()
    sleep(K)
    
'''
def make_1080p():
    cap.set(3,1920)
    cap.set(4,1920)
def make_720p():
    cap.set(3,1280)
    cap.set(4,720)
def make_480p():
    cap.set(3,640)
    cap.set(4,480)
def change_res(width,hight):
    cap.set(3,width)
    cap.set(4,height)'''

    
