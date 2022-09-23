import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import time
import requests
import threading

''' 
print(f"Altura (height): {img.shape[0]} pixels" )
print(f"Largura (width): {img.shape[1]} pixels")
'''
stop = 'start'


def varSC(stop):
    globals()['stop'] = stop


def post(text):
    requests.post("https://test7.lucasteixeira23.repl.co/r", json=text)


def servos_control(cam=0):
    pTime = 0
    width = 640
    height = 480

    cap = cv2.VideoCapture(cam)
    cap.set(3, width)
    cap.set(4, height)
    cap.set(15, 0.1)

    qx1 = int(width * 0.15)
    qy1 = int(height * 0.15)
    qx2 = int(width * 0.85)
    qy2 = int(height * 0.85)

    detector = HandDetector(detectionCon=0.5, maxHands=1)

    while True:
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

            if y2 > 240 and length < 30:
                cv2.putText(img, f'Para Baixo', (440, 290), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
                threading.Thread(target=post, args=["descer garra"]).start()

            if y2 <= 240 and length < 30:
                cv2.putText(img, f'Para Cima', (440, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
                threading.Thread(target=post, args=["subir garra"]).start()

        cv2.rectangle(img, (qx1, qy1), (qx2, qy2), (0, 255, 0))
        cv2.line(img, (0, 240), (640, 240), (255, 0, 255), 1)

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

    cv2.destroyAllWindows()


if __name__ == "__main__":
    servos_control()
