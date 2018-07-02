import cv2
import numpy as np
img = cv2.imread('/home/manpreet/mps/campture2018-06-29 08:33:24.858930.png', cv2.IMREAD_COLOR)

cv2.line(img,(256,1500),(150,150),(1,205,150),9)
#line(img,startpt,endpt,color,pointerwidth)

cv2.rectangle(img,(200,150),(210,160),(0,0,255),1)
#reactangle(img,digonlastartpt,digonalendpt,color,pointerwidth)

cv2.circle(img, (447, 63), 63, (150, 56, 255), 5)
#circle(img,center,rad,color,pointerwidth)

cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)


pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Manpreet Singh',(10,150), font, 2,(255,255,255),3,cv2.LINE_AA)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()