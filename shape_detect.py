#!/usr/bin/env python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def circleDetect():


def squareDetect():


while True:
	ret, frame = cap.read()

	circleDetect()

	squareDetect()

	cv2.imshow('frame', frame)

	cv2.waitKey(3)

cap.release()
cv2.destroyAllWindows()