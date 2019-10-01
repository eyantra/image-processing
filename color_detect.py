#!/usr/bin/env python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def greenCircleDetect():


def redCircleDetect():


def blueCircleDetect():


while True:
	ret, frame = cap.read()

	greenCircleDetect()

	redCircleDetect()

	blueCircleDetect()


	cv2.imshow('frame', frame)

	cv2.waitKey(3)

cap.release()
cv2.destroyAllWindows()