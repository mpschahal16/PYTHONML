import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread("/home/manpreet/mps/campture2018-06-29 08:33:24.858930.png",0)
rows,col=img.shape

m=np.float32([[1,0,0],[0,1,0]])
dst=cv2.warpAffine(img,m,(col,rows))
#https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/warp_affine/warp_affine.html

#It is any transformation that can be expressed in the form of a matrix multiplication (linear transformation)
#  followed by a vector addition (translation). similar to transformation studied in computer graphic



#img=cv2.flip(img,22)
plt.imshow(dst,cmap='gray',interpolation=cv2.INTER_CUBIC)
plt.xticks([]),plt.yticks([])
plt.show()