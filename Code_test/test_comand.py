import sys, time
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import time
# numpy and scipy-----
import numpy as np
# OpenCV -------------
import cv2
#---------------------
import socket
import json
#---------------------
from laneline import *
from pointLib import *

def cal_undistort(img, objpoints, imgpoints):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None,None)
    undist = cv2.undistort(img, mtx, dist, None, mtx)
    return undist, mtx, dist

if __name__ == "__main__":
    imgOri = cv2.imread('../Unity_UITCar/Window/window_version_Data/Snapshots/fx_UIT_Car.png')
    img = cv2.resize(imgOri, (640, 480))
    img_detect = ColorFilter(img)
    
    cv2.imshow('show', img_detect)
    print(img_detect.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()