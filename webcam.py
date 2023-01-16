import cv2, sys, numpy, os

class bob.db.casia_fasd.Database(foldsdir=None)[source]
Bases: object

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)
while True:
	(_, im) = webcam.read()
	gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in faces:
		cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
		cv2.putText(im, 'recognized', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
		cv2.imshow('OpenCV', im)
	
	key = cv2.waitKey(10)
	if key == 27:
		break
