import cv2
import numpy as np

drawing=False
mode=False
ix,iy=-1,-1

def drawcircle(event,x,y,flags,params):
    global ix,iy,drawing,mode
    if event==cv2.EVENT_LBUTTONDOWN:
        print("llmousebt")
        drawing=True
        ix,iy=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
                print("llmousemove++++++rect",drawing,mode)

            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
                print("llmousemove++++++circ", drawing, mode)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            print("llmouseup++++++rect", drawing, mode)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
            print("llmouseup++++++circ", drawing, mode)

img=np.zeros((512,512,4),np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback('image',drawcircle)

while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(20) &0xff
    if k==ord('m'):
        mode=not mode
    elif k==ord('q'):
        break

cv2.destroyAllWindows()
