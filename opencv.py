import cv2


img = cv2.imread('picture/shakira.jpeg',1)
img = cv2.resize(img,(200,200))
#print(type(img))
#img = cv2.rotate(img,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()