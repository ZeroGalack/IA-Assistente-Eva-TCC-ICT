import cv2
from computer_vision.face_rec.simple_facerec import SimpleFacerec

sfr = SimpleFacerec()
sfr.load_encoding_images("computer_vision/face_rec/images/")


def FaceIndetification(cam=0):
    print('Iniciando FaceID...')
    cap = cv2.VideoCapture(cam)
    while True:
        ret, frame = cap.read()
        frame_flip = cv2.flip(frame, 1)
        frame = frame_flip

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):

            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

            if name == 'Unknown':
                print("desconhecido!")
                return name

            if name != 'Unknown':
                print(name)
                cap.release()
                cv2.destroyAllWindows()
                return name

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) == ord('f'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    FaceIndetification()