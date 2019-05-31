import math
import matplotlib.pyplot as plt 
# numpy and scipy-----
import numpy as np
# OpenCV -------------
import cv2

def Finding_left_point(X_axisf, Y_axisf, image):
	Center_Yf = int(Y_axisf/2)
	Center_Xf = int(X_axisf/2)

	for i in range(Center_Yf, -1, -3):
		if (np.sum(image[(X_axisf-3):X_axisf, (i-3):i] ) > (255*5)):
			return [X_axisf, i]

	for i in range(X_axisf, -1, -3):
		if (np.sum(image[(i-3):(i), (0):(2)]) > 255*5):
			return [i, 0]

	for i in range(0, Center_Yf, 3):
		if (np.sum(image[(0):(2), (i):(i+3)]) > 255*5):
			return [0, i]
	return -1


def Finding_right_point(X_axisr, Y_axisr, image):

	Center_Yr = int(Y_axisr/2)
	Center_Xr = int(X_axisr/2)

	for i in range(Center_Yr, Y_axisr, 3):
		if (np.sum(image[(X_axisr):(X_axisr+3), (i):(i+3)]) > (255*5)):
			return [X_axisr, i]

	for i in range(Y_axisr, -1, -3):
		if (np.sum(image[(i-3):(i), (Y_axisr-3):(Y_axisr)]) > 255*5):
			return [i, Y_axisr]

	for i in range(Y_axisr, Center_Yr, -3):
		if (np.sum(image[(0):(2), (i-3):(i)]) > 255*5):
			return [0, i]
	return -1

def Angle(x_a, y_a, img_detect):
	left = Finding_left_point(x_a,y_a, img_detect)
	right = Finding_right_point(x_a,y_a, img_detect)

	if (left != -1) & (right != -1):
		cv2.line(img_detect, (left[1], left[0]), (right[1], right[0]), 255, 5)

		Coss = abs((right[1] - left[1])/(math.sqrt(pow(left[0]-right[0],2) + pow(left[1] - right[1],2))))

		angle = (math.acos(Coss)*180)/math.pi

		if (left[0] > right[0]):
			return angle
		else:
			if (left[0] < right[0]):
				return -angle
	else:
		if (left == -1):
			return -45
		else:
			return 45
