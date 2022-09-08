import cv2

file_path = '../../assets/img/496812956114780160-BuSwJnRCQAAPP1p.jpg'

# To actually visualize the effect of `CHAIN_APPROX_SIMPLE`, we need a proper image
image1 = cv2.imread(file_path)

img_gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img_gray1, 150, 255, cv2.THRESH_BINARY)
contours2, hierarchy2 = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

image_copy2 = image1.copy()

cv2.drawContours(image_copy2, contours2, -1, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('SIMPLE Approximation contours', image_copy2)
cv2.waitKey(0)

image_copy = image1.copy()

for i, contour in enumerate(contours2):  # Loop over one contour area
    for j, contour_point in enumerate(contour):  # Loop over the points
        # Draw a circle on the current contour coordinate
        cv2.circle(image_copy, (contour_point[0][0], contour_point[0][1]), 2, (0, 255, 0), 2, cv2.LINE_AA)

# See the results
cv2.imshow('CHAIN_APPROX_SIMPLE Point only', image_copy)
cv2.waitKey(0)
cv2.imwrite('contour_detection_simple.jpg', image_copy)
cv2.destroyAllWindows()
