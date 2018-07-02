import cv2
import numpy as np

faceDetect=cv2.CascadeClassifier('/home/manpreet/PycharmProjects/mps/PYTHONML/extradirforfile/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

while True:
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5, minSize=(30, 30),
                                        )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Faces",img)
    if (cv2.waitKey(1)== ord('q')):
        break

cam.release()
cv2.destroyAllWindows()