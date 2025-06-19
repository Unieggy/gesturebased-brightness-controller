import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, modelcomplex=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelcomplex = modelcomplex
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelcomplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def handDetect(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)



    def positionLocate(self,img,hand=0):
        lmList=[]
        if self.results.multi_hand_landmarks:
            numhand=self.results.multi_hand_landmarks[hand]
            for id, lm in enumerate(numhand.landmark):
                l, w, c = img.shape
                x, y = int(lm.x * w), int(lm.y * l)
                lmList.append([id,x,y])
                cv2.circle(img, (x, y), 9, (222, 80, 0), cv2.FILLED)
        return lmList



def main():
    ptime = 0
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        ctime=time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (133, 0, 2), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
    