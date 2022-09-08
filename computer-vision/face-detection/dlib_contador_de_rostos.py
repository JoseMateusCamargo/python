import cv2
import numpy as np
import dlib  # pip install dlib

"""
Install-dlib
Download and Credits: https://github.com/datamagic2020/Install-dlib
python 3.8 : pip install dlib-19.19.0-cp38-cp38-win_amd64.whl
python 3.9 : pip install dlib-19.22.99-cp39-cp39-win_amd64.whl
python 3.10 : pip install dlib-19.22.99-cp310-cp310-win_amd64.whl
"""

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    i = 0

    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
        i = i + 1
        cv2.putText(frame, 'face num' + str(i), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print(face, i)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
