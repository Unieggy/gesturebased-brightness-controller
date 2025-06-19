import math
import cv2
import mediapipe as mp
import time
import handmodule as hm
import screen_brightness_control as sbc
import numpy as np
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


Widthcam,Heightcam=640,480
ptime = 0
cap = cv2.VideoCapture(0)
detector = hm.handDetector(detectionCon=0.7,trackCon=0.7)
cap.set(3,Widthcam)
cap.set(4,Heightcam)
while True:
    success, img = cap.read()
    detector.handDetect(img)
    locationList=detector.positionLocate(img,hand=0)


    if len(locationList)!=0:
        x1,y1=locationList[4][1],locationList[4][2]
        x2,y2=locationList[8][1],locationList[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2
        cv2.circle(img,(x1,y1),10,(2,23,200),3,cv2.FILLED)
        cv2.circle(img,(x2,y2),10,(2,255,10),3,cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(23,80,0),4)
        length=math.hypot(x1-x2,y1-y2)
        print(length)
        if length<=30:
            cv2.circle(img,(cx,cy),8,(0,0,255),8,cv2.FILLED)
            length=0
        #brightness_adj = np.interp(length, [30, 220], [min, max])
        #sbc.set_brightness(value=brightness_adj)

    ctime=time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (133, 0, 2), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)