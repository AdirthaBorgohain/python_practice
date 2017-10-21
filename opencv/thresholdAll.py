#threshold in  opencv
#simplyifing a image
#the image is either a 0/1 or white/black

import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')

#color threshold
#below 12 all will be black and above 12 will be white
retval, threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)


#grayscaled threshold
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)



'''since in the grayscaled threshold some parts are very blackwe will use gaussian threshold'''
gaus =cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow('threshold2',threshold2)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('adaptivethreshold',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()


