#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2021-03-08
@author: JMC
Simple script to open image, access pixel, make rectangle and set text at image.
"""

import cv2

# Read image
img = cv2.imread("img/496812956114780160-BuSwJnRCQAAPP1p.jpg")

img_cp = img.copy()
print(img_cp.shape)

# Access the pixel where x = 115 and y = 5
access = img_cp[115, 5]
print("Access color in pixel: %s " % access)
print("Blue: %s, Green: %s, Red: %s" % (access[0], access[1], access[2]))

# Start coordinate, represents the top left corner of rectangle
start_point = (115, 5)

# Ending coordinate, represents the bottom right corner of rectangle
end_point = (250, 139)

# Green color in BGR
color = (0, 255, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(img_cp, start_point, end_point, color, thickness)

# Set text
font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image, 'OMG!', (115, 165), font, 1, color, 2, cv2.LINE_AA)

cv2.imshow('image', img_cp)
cv2.waitKey(0)
cv2.destroyAllWindows()
