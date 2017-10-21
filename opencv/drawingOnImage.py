#shows hot to draw line ,circle,rectangle,polygon in opencv


import numpy as np
import cv2

#opens an image named applr.jpg are reads it in color mode
img = cv2.imread('apple.jpg',cv2.IMREAD_COLOR)


#draws a line on the image starting from (0,0) to (150,150)
#and bgr values of 255,255,255(white) and thickness 15
cv2.line(img ,(0,0), (450,450), (255,255,255),15)


#draws a rectangle starting from topleft=15,25 to topright= 200,150
cv2.rectangle(img,(70,25),(500,650),(0,255,0),5)


#draws a circle img,centre,radius,color,-1 to fill it
cv2.circle(img,(100,63),55,(0,0,255),-1)

#drawing a polygon

#puts the points in a numpy 2d array convert it to int32
pts=np.array([[20,40],[100,150],[205,256],[400,100],[55,55]],np.int32)
#put the imagepointer, numpy array, true stands for connecting
#the end point to the starting point and 3 is the thickness
cv2.polylines(img,[pts], True , (0,255,255) ,3 )


#writing on a image
font = cv2.FONT_HERSHEY_SIMPLEX
#img is the image pointer,text,startpoint,font,fontSize,color,width,anti_aliasing
cv2.putText(img,'Opencv Nitya',(0,130),font,4.3,(200,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
