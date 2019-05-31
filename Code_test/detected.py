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

if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip , port))
        print("Connected to ", ip, ":", port)

        ## image processing here
    except Exception as ex:
        print(ex)
        sys.exit()

    while (True):
        try:
            # imgOri = cv2.imread('../Unity_UITCar/Window/window_version_Data/Snapshots/fx_UIT_Car.png')
            imgOri = cv2.imread('../../../Window/Computer_Vision/Unity_UITCar/Round3/window_version_Data/Snapshots/fx_UIT_Car.png')
            img = cv2.resize(imgOri, (640, 480))
            img_detect = ColorFilter(img)
            angle = Angle(177,637, img_detect)

            if (angle == None):
            	message = jsonToString(0, 0)
            	#message = "Hello World"
            	arr = bytes(message, 'ascii')
            	sock.sendall(arr)
            else:
            	message = jsonToString(30, angle)
            	#message = "Hello World"
            	arr = bytes(message, 'ascii')
            	sock.sendall(arr)
            cv2.imshow('show', img_detect)
            cv2.imshow('original', imgOri)
            cv2.waitKey(1)
        except Exception as ex:
            #print(ex)
            pass
#-----------------------------------------------------------------

cv2.destroyAllWindows()
