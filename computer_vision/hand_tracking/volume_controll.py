import time
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import math
import cv2
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


stop = 'start'
def varHVC(stop):
    globals()['stop'] = stop


def volume_controller(cam=0, maxhands=1):

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # volume.GetMute()
    volume.GetMasterVolumeLevel()
    volRange = volume.GetVolumeRange()
    minVol = volRange[0]
    maxVol = volRange[1]


    cap = cv2.VideoCapture(cam)
    porcentagem = 0
    pTime = 0
    detector = HandDetector(detectionCon=0.5, maxHands=maxhands)

    while 1:
        success, img = cap.read()
        img = cv2.flip(img, 1)

        hands, img = detector.findHands(img, flipType=False)
        position = detector.findPosition(img, draw=False)
        if hands:

            x1, y1 = position[4][1], position[4][2]
            x2, y2 = position[8][1], position[8][2]

            cv2.circle(img, (x1, y1), 15, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 3)

            length = math.hypot(x2 - x1, y2 - y1)
            #print(length)
            # Hand range 50 - 220
            # Volume Range -65,25 - 0

            vol = np.interp(length, [50, 220], [minVol, maxVol])
            #print(int(vol))
            volume.SetMasterVolumeLevel(int(vol), None)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

        if cv2.waitKey(1) == ord('f'):
            break

        if stop == 'stop':
            break

        cv2.imshow("Img", img)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    volume_controller()
