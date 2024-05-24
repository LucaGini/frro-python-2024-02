import numpy as np
import cv2

#capture frames from a camera
cap = cv2.VideoCapture("videoSalida.avi")
#cap = cv2.VideoCapture(0)
#read the frames from the camera
_, img = cap.read()

#modify the data type
#setting to 32-bit floating point
averageValue1 = np.float32(img)

#loop runs if capturing has been initialized
while (1):
    #reads frame from a camera
    _, img = cap.read()
    #using the cv2.accumulateWeighted() function that updates the running average
    cv2.accumulateWeighted(img, averageValue1, 0.05)
    #converting the matrix elements to absolute values and converting the result to 8bit
    resultingFrames1 = cv2.convertScaleAbs(averageValue1)
    #show two output windows the input / original frames windows
    cv2.imshow("inputWindow", img)
    #the window showing output of alpha values 0.02
    cv2.imshow("averageValue1", resultingFrames1)
    #wait for Esc key stop program
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
#Close the window
cap.release()
