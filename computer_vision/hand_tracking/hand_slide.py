import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import pyautogui


def hand_slide(cam=0):
    btleft = 0
    btright = 0

    cap = cv2.VideoCapture(cam)
    cap.set(3, 640)
    cap.set(4, 480)

    detector = HandDetector(detectionCon=0.5, maxHands=1)

    pTime = 0
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)

        hands, img = detector.findHands(img, flipType=False)
        if not hands:
            btleft = 0
            btright = 0

        if hands:

            fingers = detector.fingersUp(hands[0])
            print('fingers ' + str(fingers))

            if fingers == [1, 1, 0, 0, 0]:
                cv2.putText(img, f'-1', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 255), 3)
                btleft = btleft + 1
                print(btleft)

            if fingers == [1, 0, 0, 0, 1]:
                cv2.putText(img, f'1', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 255), 3)
                btright = btright + 1
                print(btright)

            if btleft >= 10:
                pyautogui.press('left', presses=1)
                btleft = 0

            if btright >= 10:
                pyautogui.press('right', presses=1)
                btright = 0

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

        if cv2.waitKey(1) == ord('f'):
            break

        cv2.imshow("Img", img)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    hand_slide()