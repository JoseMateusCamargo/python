import cv2

file_path = '../../assets/img/496812956114780160-BuSwJnRCQAAPP1p.jpg'

# Read the image
image = cv2.imread(file_path)

# Convert the image to grayscale format
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

'''
Agora, use a threshold()função para aplicar um limite binário à imagem. 
Qualquer pixel com um valor superior a 150 será definido com um valor de 255 (branco). 
Todos os pixels restantes na imagem resultante serão definidos como 0 (preto). 
O valor limite de 150 é um parâmetro ajustável, para que você possa fazer experiências com ele. 
'''
# Apply binary thresholding
ret, thresh = cv2.threshold(img_gray, 175, 255, cv2.THRESH_BINARY)

# Visualize the binary image
cv2.imshow('Binary image', thresh)
cv2.waitKey(0)

# cv2.imwrite('image_thres1.jpg', thresh) # Use to save
cv2.destroyAllWindows()

# Detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# Draw contours on the original image
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                 lineType=cv2.LINE_AA)

# See the results
cv2.imshow('CHAIN_APPROX_NONE', image_copy)
cv2.waitKey(0)
cv2.imwrite('contour_detection_none.jpg', image_copy)
cv2.destroyAllWindows()
