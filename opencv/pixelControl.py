#controling the pixels of an image

import numpy as np
import cv2

img=cv2.imread('apple.jpg',cv2.IMREAD_COLOR)
#reads the image in color


#reference a pixel
#px=img [55,55]
#check thr bgr valus of that pixel using print(px)


#converting the color of that pixel

#ROI=region of an image

#convering color of pixels
#img[row:row+height,column:column+width]=color
img[100:150 ,100:150]=[255,255,255]


#copying a part of image and pasting it in some other else part
apple_part=img[100:200,150:210]
#200-100=100
#210-150=60
img[0:100,0:60]=apple_part

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


