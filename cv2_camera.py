#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on ‎quarta-feira, ‎29‎ de ‎julho‎ de ‎2020, ‏‎18:55:35
@author: JMC
Open camera
"""

import cv2

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):  # q -> to close
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
