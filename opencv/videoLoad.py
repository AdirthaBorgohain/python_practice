import numpy as np
import cv2


#captue will store the frames from camers
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    

    #applying a gray filter to the frames
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Display the  frame with colors 
    cv2.imshow('frame',frame)

    #display the frame in grayscale
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

