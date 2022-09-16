import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import serial
import time

pTime = 0
try:
    serial.Serial('COM9', 9600).close()
    PortaSerial = serial.Serial('COM9', 9600)
    print('arduino ok')

except serial.serialutil.SerialException:
    print('arduino n ok')


'''def arduino(codigo):
    try:
        cod = str(codigo) # O # para separar as mensagens
        print(cod)
        PortaSerial.write(cod.encode())# Funçao que envia a mesagem pela porta serial 'utf-8'
        #PortaSerial.flush()

    except AttributeError:
        print('arduino não conectado')'''

def arduino(codigo):
    try:
        cod = str(codigo)+'#'; # O # para separar as mensagens
        PortaSerial.write(cod.encode())# Funçao que envia a mesagem pela porta serial
        print(cod.encode())
        PortaSerial.flush()
    except AttributeError:
        print('arduino não conectado')

''' 
print(f"Altura (height): {img.shape[0]} pixels" )
print(f"Largura (width): {img.shape[1]} pixels")
'''
width = 640
height = 480

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
cap.set(15, 0.1)

qx1 = int(width * 0.15)
qy1 = int(height * 0.15)
qx2 = int(width * 0.85)
qy2 = int(height * 0.85)


detector = HandDetector(detectionCon=0.5)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, flipType=False)

    position = detector.findPosition(img, draw=False)

    if hands:

        fingers = detector.fingersUp(hands[0])
        x, y = position[9][1], position[9][2]

        #print('fingersUp ' + str(fingers))
        #print(x, y)

        if fingers == [1, 0, 0, 0, 0]:
            cv2.putText(img, f'Garra fechada', (100, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            globals()['garra'] = 0

        if fingers == [0, 1, 1, 1, 1]:
            cv2.putText(img, f'Garra Aberta', (100, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            globals()['garra'] = 1

        cv2.rectangle(img, (qx1, qy1), (qx2, qy2), (0, 255, 0))

        px = int(np.interp(x, [qx1, qx2], [0, 180]))#int(((10*x)/44)-22)
        #print(px)
        #arduino(px)

        py = int(np.interp(y, [qy1, qy2], [180, 0]))
        #print(py)
        vl = str(px)+'-'+str(py)+':'
        arduino(vl)
        time.sleep(1)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)


    if cv2.waitKey(1) == ord('f'):
        break

    cv2.imshow("Img", img)
    cv2.waitKey(1)

cv2.destroyAllWindows()
