import numpy as np
import cv2


#ur1="https://www.google.com"
#webbrowser.open(ur1)

cap=cv2.VideoCapture(0)
img_count=0
    
        
def rescale_frame(frame,procent=75):
    #scale_procent=75
    width = int(frame.shape[1]*procent/100)
    height= int(frame.shape[0]*procent/100)
    dim=(width,height)
    return(cv2.resize(frame,dim,interpolation=cv2.INTER_AREA))

while True:
    ret,frame=cap.read()
    if not ret:
        break
    frame = rescale_frame(frame,procent=100)
    cv2.imshow("capturing",frame)
    #frame2= rescale_frame(frame,procent=50)
    #cv2.imshow("test2",frame2)

    if cv2.waitKey(33)== 27:
        break
    elif cv2.waitKey(33)==32:
        #screenshot(frame)
        img_name="picture_{}.png".format(img_count)
        cv2.imwrite(img_name,frame)
        img_count+=1
        print("screeenshot taken")

    
cap.release()
cv2.destroyAllWindows()