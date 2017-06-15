import cv2
import os
import numpy as np 
from PIL import Image

recognizer = cv2.face.createLBPHFaceRecognizer()
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def getImageAndLabels(path):
    ImagePaths = [os.path.join(path,files) for files in os.listdir(path)]
    samples = []
    Ids = []
    for imgpath in ImagePaths:
        pilImage = Image.open(imgpath).convert('L')
        imgArray = np.array(pilImage,'uint8')
        Id=int(os.path.split(imgpath)[-1].split(".")[1])
        faces=face_detector.detectMultiScale(imgArray)
        for (x,y,w,h) in faces:
            samples.append(imgArray[y:y+h,x:x+w])
            Ids.append(Id)
    return samples,Ids

face, Ids = getImageAndLabels('face_data')
recognizer.train(face,np.array(Ids))
recognizer.save('trained_data/trainer.yml') 
