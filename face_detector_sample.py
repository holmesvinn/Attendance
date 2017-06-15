import cv2
import numpy as np 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 3)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(120,56,144),10)     
    cv2.imshow('img',img)
    if  cv2.waitKey(1) & 0xff == ord('q'):
        break 
           
cap.release()
cv2.destroyAllWindows()