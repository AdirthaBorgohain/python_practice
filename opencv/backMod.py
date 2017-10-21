#this program cuts the logo from mainlogo.png removes the background and puts it on 3D-Matplotlib.png


import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

#getting the no of rows cols and hannels from img2
rows,cols,channels = img2.shape

#sice we want to put the logo in top left corener
#our region of interest it the top left
# so img1[row:row+height,col:col+width]
roi = img1[0:rows,0:cols]

#converting the logo to gray
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#if below 220 its converted to black
#if below 255 its converted to 255
ret, mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

#we invert the mas so white will be black and black will be white
mask_inv = cv2.bitwise_not(mask)

img1_backgd = cv2.bitwise_and(roi,roi,mask=mask_inv)

cv2.imshow('bcgd',img1_backgd)
img2_forgd= cv2.bitwise_and(img2,img2,mask=mask)

cv2.imshow('fgd',img2_forgd)

dst = cv2.add(img1_backgd,img2_forgd)

img1[0:rows,0:cols]= dst

cv2.imshow('finaal',img1)

#cv2.imshow('mask',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

