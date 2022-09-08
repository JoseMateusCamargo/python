import pywhatkit as kit
import cv2

# Convert Text to Hand Written Text
kit.text_to_handwriting("Hope you are doing well", "handwriting.png", (18, 10, 143))
img = cv2.imread("handwriting.png")

cv2.imshow("Text to Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
