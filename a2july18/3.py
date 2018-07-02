import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread("/home/manpreet/mps/campture2018-06-29 08:33:24.858930.png",0)
rows,col=img.shape

m=np.float32([[1,0,100],[0,1,50]])
dst=cv2.warpAffine(img,m,(col,rows))
#img=cv2.flip(img,22)
plt.imshow(dst,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()