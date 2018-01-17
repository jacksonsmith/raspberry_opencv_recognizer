import cv2,os
import numpy as np
from PIL import Image 
import pickle
import os
from time import sleep

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainer/trainer.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'
deniedAccessCount = 0
cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) #Creates a font
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
	
	name = 'desconhecido'

        if(nbr_predicted==7 and conf < 60.0 ):
             name='Jackson'
        elif(nbr_predicted==55 and conf < 60.0 ):
             name='Edivaldo'
	     os.system("python servo_garagem_abre.py")
	     sleep(0.5) 
	     os.system("python servo_garagem_fecha.py")
	else:
	     print("teste")
	     deniedAccessCount += 1
	     print("conf: " + str(conf))



	if deniedAccessCount >= 100:
		os.system("python mail.py")
		deniedAccessCount = 0
        cv2.cv.PutText(cv2.cv.fromarray(im),str(name), (x,y+h),font, 255) #Draw the text
        cv2.imshow('im',im)
        cv2.waitKey(5)





