import cv2
from cvzone.HandTrackingModule import HandDetector
import time


stop = 'start'
def varHS(stop):
    globals()['stop'] = stop


def hand_sinais(cam=0):

    cap = cv2.VideoCapture(cam)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=0.5, maxHands=2)

    pTime = 0
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)

        hands, img = detector.findHands(img, flipType=False)

        if hands:

            fingers = detector.fingersUp(hands[0])
            fingers2 = detector.fingersUp(hands[-1])
            print('fingers ' + str(fingers))
            print('fingers2 ' + str(fingers2))

            if fingers == [1, 0, 0, 0, 0] and fingers2 == [1, 0, 0, 0, 0]:
                cv2.putText(img, f'0', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 255), 3)

            if fingers == [1, 1, 0, 0, 0] and fingers2 == [1, 1, 0, 0, 0]:
                cv2.putText(img, f'1', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 255), 3)

            if fingers == [1, 1, 1, 0, 0] and fingers2 == [1, 1, 1, 0, 0]:
                cv2.putText(img, f'2', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 255), 3)

            if fingers == [1, 1, 1, 1, 0] and fingers2 == [1, 1, 1, 1, 0]:
                cv2.putText(img, f'3', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 255), 3)

            if fingers == [1, 1, 1, 1, 1] and fingers2 == [1, 1, 1, 1, 1]:
                cv2.putText(img, f'4', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 255), 3)

            if fingers == [0, 1, 1, 1, 1] and fingers2 == [0, 1, 1, 1, 1]:
                cv2.putText(img, f'5', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 255), 3)

            # a apartir do 6 inverte!!!
            if fingers2 == [0, 1, 1, 1, 1] and fingers == [1, 1, 0, 0, 0]:
                cv2.putText(img, f'6', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 6, (0, 0, 255), 3)

            if fingers2 == [0, 1, 1, 1, 1] and fingers == [1, 1, 1, 0, 0]:
                cv2.putText(img, f'7', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 6, (0, 0, 255), 3)

            if fingers2 == [0, 1, 1, 1, 1] and fingers == [1, 1, 1, 1, 0]:
                cv2.putText(img, f'8', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 6, (0, 0, 255), 3)

            if fingers2 == [0, 1, 1, 1, 1] and fingers == [1, 1, 1, 1, 1]:
                cv2.putText(img, f'9', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 6, (0, 0, 255), 3)

            #erros
            if fingers2 == [1, 0, 0, 0, 0] and fingers == [1, 1, 0, 0, 0]:
                cv2.putText(img, f'10', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 6, (0, 0, 255), 3)

            #frase
            if fingers == [1, 1, 0, 0, 1]:
                cv2.putText(img, f'Rock and roll', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 3)

            if fingers2 == [0, 0, 0, 0, 0] and fingers == [0, 0, 0, 0, 0]:
                cv2.putText(img, f'Like', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 3)

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
    hand_sinais()