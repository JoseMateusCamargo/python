import cv2
import sys
import os

# path_image = sys.argv[1] # Passing the image for parameter
path_image = '../../assets/img/group.jpg'

cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
path_cascade = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(path_cascade)
image = cv2.imread(path_image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30), )

print(f'Found {len(faces)} faces!')

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Faces found', image)
cv2.waitKey(0)
