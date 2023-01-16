
import cv2, sys, numpy as np, os
from PIL import Image
from pathlib import Path
# print("File      Path:", Path(__file__).absolute())


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

count = 0
# Parent Directory path 
parent_dir = Path().absolute()
filename = str(parent_dir)+"/me2.jpg"

img = Image.open(filename)
image_data = np.asarray(img)
w, h = img.size
print(img.size)
gray = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(image_data, 1.3, 5)
for (x, y, w, h) in faces:
	cv2.rectangle(image_data, (x, y), (x + w, y + h), (255, 0, 0), 2)
	cv2.putText(image_data, 'recognized', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

	# save image to directory
	directory = input("\n enter name of the subject : ")
	# Path 
	path = os.path.join(parent_dir, directory) 

	# Create the directory 
	new_path = os.mkdir(path) 
	print("Directory '% s' created" % directory) 
	print(path)

	# save imahe
	cv2.imwrite(str(path) + '/face_' + str(count) + ".jpg", gray[y:y+h,x:x+w])
	count +=1


	# split() method
	# Save Chops of original image
	width, height = x + w, y + h
	chopsize = 25
	for x0 in range(0, width, chopsize):
		for y0 in range(0, height, chopsize):
			box = (x0, y0,
					x0+chopsize if x0+chopsize <  width else  width - 1,
					y0+chopsize if y0+chopsize < height else height - 1)
			# save imahe
			patchname = str(path) + '/patch_' + str(count) + str(x0) +"_"+ str(y0) + ".jpg"
			img.crop(box).save(patchname)

