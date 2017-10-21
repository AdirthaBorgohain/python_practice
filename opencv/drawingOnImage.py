import numpy as np
import cv2

#opens an image named applr.jpg are reads it in color mode
img = cv2.imread('apple.jpg',cv2.IMREAD_COLOR)


#draws a line on the image starting from (0,0) to (150,150)
#and bgr values of 255,255,255(white) and thickness 15
cv2.line(img ,(0,0), (150,150), (255,255,255),15)


#draws a rectangle starting from topleft=15,25 to topright= 200,150
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)


#draws a circle img,centre,radius,color,-1 to fill it
cv2.circle(img,(100,63),55,(0,0,255),-1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
