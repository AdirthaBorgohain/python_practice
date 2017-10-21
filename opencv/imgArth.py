#uncomment the middle lines to use the functions

import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')


'''adding the both images img1 and img2 should be of same sizes


add = img1 + img2  


'''

'''using opencv add functions


add = cv2.add(img1,img2)


opencv add function add the pixel values and not the images'''

'''This weighted function also add the image but with weight)'''
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

'''cv2.imshow('add',add)'''
cv2.imshow('weight',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows();
