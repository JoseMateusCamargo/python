import cv2
import os

cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
path_cascade = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')

# Load the cascade
face_cascade = cv2.CascadeClassifier(path_cascade)

# To capture the video frame
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('file_name.mp4')

while True:
    # Read the frame
    _, img = cap.read()

    # Covert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # Draw the rectangle around each face
    for [x, y, w, h] in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
