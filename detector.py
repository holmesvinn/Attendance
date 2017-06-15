import cv2
import numpy as np
import sqlite3 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('trained_data\\trainer.yml')

def getDetails(id):
    conn = sqlite3.connect("studentsFaceData.db")
    cmd = "SELECT * FROM students WHERE roll="+str(id)
    cursor = conn.execute(cmd)
    details = "Null"
    for row in cursor:
        details = row
    conn.close()
    return details

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 3)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(120,56,144),1) 
        id,config = recognizer.predict(gray[y:y+h,x:x+w])
        print(id)
        print(config)
        details = getDetails(id)
        if(details != "Null"):
            cv2.putText(img, str(details[1]), (x+w,y+30),font, 1 , (0,0,0), 1)
            cv2.putText(img, str(details[2]), (x+w,y+90),font, 1 , (0,0,0), 1)
            cv2.putText(img, str(details[3]), (x+w,y+50),font, 1 , (0,0,0), 1)
            cv2.putText(img, str(details[4]), (x+w,y+70),font, 1 , (0,0,0), 1)
        else:
            cv2.putText(img,"Unknown", (x,y),font, 1 , (255,255,0), 1)


    cv2.imshow('img',img)
    if  cv2.waitKey(1) & 0xff == ord('q'):
        break 
           
cap.release()
cv2.destroyAllWindows()