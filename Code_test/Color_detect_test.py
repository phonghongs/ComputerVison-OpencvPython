import sys, time
import math
import matplotlib.pyplot as plt
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

#---------------------	Socket 	-------------------
def jsonToString(speed, angle):
    jsonObject = {
        'speed': speed,
        'angle': angle,
    }

    jsonString = json.dumps(jsonObject)
    print(jsonString)
    return jsonString

port = 9999
ip = str(sys.argv[1])
def nothing(x):
    pass

cv2.namedWindow("Trackbars")

cv2.createTrackbar("L - H", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

def main():
    while (True):
        try:
            imgOri = cv2.imread('../Unity_UITCar/Window/window_version_Data/Snapshots/fx_UIT_Car.png')

            hsv = cv2.cvtColor(imgOri, cv2.COLOR_BGR2HSV)
            l_h = cv2.getTrackbarPos("L - H", "Trackbars")
            l_s = cv2.getTrackbarPos("L - S", "Trackbars")
            l_v = cv2.getTrackbarPos("L - V", "Trackbars")
            u_h = cv2.getTrackbarPos("U - H", "Trackbars")
            u_s = cv2.getTrackbarPos("U - S", "Trackbars")
            u_v = cv2.getTrackbarPos("U - V", "Trackbars")

            lower = np.array([l_h, l_s, l_v])
            upper = np.array([u_h, u_s, u_v])

            mask = cv2.inRange(hsv, lower, upper)

            result = cv2.bitwise_and(imgOri, imgOri, mask = mask)
            cv2.imshow("image", result)
            print(l_h, l_s, l_v, "   ", u_h, u_s, u_v)
            cv2.waitKey(1)
            
        except Exception as ex:
            pass

if __name__ == "__main__":
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip , port))
        print("Connected to ", ip, ":", port)

        ## image processing here
    except Exception as ex:
        print(ex)
        sys.exit()
    main()

cv2.destroyAllWindows()