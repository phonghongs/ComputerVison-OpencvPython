import math
import matplotlib.pyplot as plt
# numpy and scipy-----
import numpy as np
# OpenCV -------------
import cv2

def Cannyfilter(image):
	img2Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(img2Gray, (5,5), 0)
	canny = cv2.Canny(blur, 250, 255)
	return canny

def ColorFilter(image):
	blur = cv2.GaussianBlur(image, (5,5), 0)
	HSV	= cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

	# lower_line = np.array([60,0,170])
	# upper_line = np.array([150,255,255])
	# mask_line = cv2.inRange(HSV, lower_line, upper_line)

	# lower_shadow = np.array([80,60,80])
	# upper_shadow = np.array([220,190,250])
	lower_line = np.array([0,0,182])
	upper_line = np.array([107,23,255])
	mask_line = cv2.inRange(HSV, lower_line, upper_line)

	lower_shadow = np.array([101, 80, 112])
	upper_shadow = np.array([107, 98, 154])

	mask_shadow = cv2.inRange(HSV, lower_shadow, upper_shadow)

	combo_mask = cv2.bitwise_or(mask_line, mask_shadow)
	mask_inv = combo_mask[300:]
	
	return mask_inv
#----------------------------------------------------


def PointLane(image, device):
	X, Y = image.shape
	imgBGR = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

	stepx = int(X/device)
	stepy = 2;
	# X device into step time
	A = [[] for _ in range(device)]
	countX = 0;
	#duyet tu tren duyet xuong, kiem tra 1 o 10*2 pixel
	for i in range(0, X, stepx):
		for j in range(0, Y, stepy):
			pixel = np.sum(image[(i):(i+10) , j:(j+2)])
			A[countX].append(pixel)
			if pixel > 2500 :
				imgBGR[(i):(i+10) , j:(j+2)] =  [0,255,0]
		countX +=1
	print(A)
	return imgBGR



def LineCenter(image, device):
	X, Y = image.shape
	imgBGR = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

	stepx = int(X/device)
	stepy = 2;

	# X device into step time
	PointArrayLeft = [[] for _ in range(2)]
	PointArrayRight = [[]for _ in range(2)]
	PointAlong = [[]for _ in range(2)]

	CheckPoint1 = False

	countX = 0
	line = 0
	#duyet tu tren duyet xuong, kiem tra 1 o 10*2 pixel
	for i in range(0, X, stepx):
		max = 0	#kiem tra khoang pixel lon nhat tren line
		check_point = False
		CheckPoint2 = False

		CacheX1 = 0
		CacheY1 = 0
		CacheX2 = 0
		CacheY2 = 0

		for j in range(0, Y, stepy):
			pixel = np.sum(image[(i):(i+10) , j:(j+2)])
			print(pixel)
			if pixel > max:	#kiem tra line max, neu xuat hien line thi set check_point = true
				max = pixel
				CacheX1 = i
				CacheY1 = j
				check_point = True

			if (pixel == 0) & (check_point == True):
				check_point = False
				if (CheckPoint1 == True):

					imgBGR[(CacheX):(CacheX+10) , CacheY:(CacheY+10)] =  [0,255,0]
					max = 0

			# if (pixel == 0) & (check_point == True):
			# 	check_point = False
			# 	max =0
			#
			# 	if (CheckPoint2 == False):
			# 		if (left != 0):
			# 			PointArrayLeft[0].append(i)
			# 			PointArrayLeft[1].append(j)
			# 			CheckPoint2 = True
			# 			imgBGR[(i):(i+10) , j:(j+2)] =  [0,255,0]
			# 		else:
			# 			if right != 0:
			# 				PointArrayRight[0].append(i)
			# 				PointArrayRight[1].append(j)
			# 				countX +=1
			# 				imgBGR[(i):(i+10) , j:(j+2)] =  [255,0,0]
			# 				break
			#
			# 	if (CheckPoint2 == True ):
			# 		PointArrayRight[0].append(i)
			# 		PointArrayRight[1].append(j)
			# 		imgBGR[(i):(i+10) , j:(j+2)] =  [255,0,0]
			# 	# If countX =0----------------------------
			# 	if (countX == 0) & (CheckPoint1 == False):
			# 		Cache = j
			# 		CheckPoint1 = True
			# 	else:
			# 		if (CheckPoint2 == True):
			# 			PointArrayLeft[0].append(i)
			# 			PointArrayLeft[1].append(Cache)
			# 			PointArrayRight[0].append(i)
			# 			PointArrayRight[1].append(j)
			# 			imgBGR[(i):(i+10) , j:(j+2)] =  [255,0,0]
			# 			imgBGR[(i):(i+10) , Cache:(Cache+2)] =  [0,255,0]
			# 			right += 1
			# 			left += 1
			# 			break
			# 		else:
			# 			if (countX == 0) & (CheckPoint1 == True):
			# 				if (j < Cache):
			# 					PointArrayLeft[0].append(i-1)
			# 					PointArrayLeft[1].append(Cache)
			# 					PointArrayLeft[0].append(i)
			# 					PointArrayLeft[1].append(j)
			# 					imgBGR[(i-1):(i-1+10) , Cache:(Cache+2)] =  [0,255,0]
			# 					imgBGR[(i):(i+10) , j:(j+2)] =  [0,255,0]
			# 					left += 1
			# 				else:
			# 					PointArrayRight[0].append(i-1)
			# 					PointArrayRight[1].append(Cache)
			# 					PointArrayRight[0].append(i)
			# 					PointArrayRight[1].append(j)
			# 					imgBGR[(i-1):(i-1+10) , Cache:(Cache+2)] =  [255,0,0]
			# 					imgBGR[(i):(i+10) , j:(j+2)] =  [255,0,0]
			# 					right += 1
			# 	countX +=1
				# print(PointArrayLeft)
				# print(PointArrayRight)
	return imgBGR
