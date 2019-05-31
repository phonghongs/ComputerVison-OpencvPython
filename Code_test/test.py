import sys, time
import math
import matplotlib.pyplot as plt
import time
# numpy and scipy-----
import numpy as np
# OpenCV -------------
import cv2 as cv
#---------------------
import socket
import json
#---------------------
from laneline import *
from pointLib import *

def nothing(x):
    pass

cv2.namedWindow("image", cv2.WINDOW_NORMAL)

cv2.createTrackbar("Threshold", "image", 0, 255, nothing)

imgOri = cv2.imread('../Unity_UITCar/Window/window_version_Data/Snapshots/fx_UIT_Car.png')

img = cv2.cvtColor(imgOri, cv2.COLOR_BGR2GRAY)

imgs = img[400:]

cv2.imshow('img', imgs)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()