import cv2
import numpy as np

def drawcircle(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),25,(255,0,0),5)

img=np.zeros((720,1280,4),np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback('image',drawcircle)

while(True):
    cv2.imshow('image',img)
    if (cv2.waitKey(20)&0xff)==ord('q'):
        print(True)
        break

cv2.destroyAllWindows()



