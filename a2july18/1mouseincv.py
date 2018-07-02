import cv2
import numpy as np

def drawcircle(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),25)


img=np.zeros((512,512,4),np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback('image',drawcircle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) &0xff=='q':
        break

cv2.destroyAllWindows()
