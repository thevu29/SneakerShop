import cv2
import face_recognition as fr
import numpy as np
import os
from tkinter import messagebox

class FaceRecognition:
    images = []
    faceLocations = []
    faceEncodings = []
    faceNames = []
    knownFaceEncodings = []
    knownFacenames = []

    def __init__(self):
        for item in os.listdir('./img/vip_customer'):
            currentImg = cv2.imread(f'./img/vip_customer/{item}')
            self.images.append(currentImg)
            self.knownFacenames.append(os.path.splitext(item)[0])

        self.encodeFaces()

    def encodeFaces(self):
        for image in self.images:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            try:
                faceEncoding = fr.face_encodings(image)[0]
                self.faceEncodings.append(faceEncoding)
            except:
                pass

    def recognition(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            messagebox.showerror('Error', 'Không thể truy cập camera')

        cnt = 0
        timeOut = False
        faceDetect = False
        face_encodings = []
        
        while cnt <= 35:
            ret, frame = cap.read()
            name = ''
            
            myFrame = cv2.resize(frame, (0, 0), None, fx=0.5, fy=0.5)
            myFrame = cv2.cvtColor(myFrame, cv2.COLOR_BGR2RGB)

            currentFaceFrame = fr.face_locations(myFrame)
            face_encodings = fr.face_encodings(myFrame, currentFaceFrame)
            
            for encodeFace in face_encodings:
                faceDis = fr.face_distance(self.faceEncodings, encodeFace)
                matchesIndex = np.argmin(faceDis)
                
                if faceDis[matchesIndex] < 0.35:
                    faceDetect = True
                    name = self.knownFacenames[matchesIndex]
                else:
                    timeOut = True
            
            for faceLocation in currentFaceFrame:
                y1, x2, y2, x1 = faceLocation
                y1, x2, y2, x1 = y1 * 2, x2 * 2, y2 * 2, x1 * 2

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
        
            cnt += 1
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        if timeOut == False:
            if faceDetect == True:
                messagebox.showinfo('Information', 'Bạn là khách hàng thành viên và được áp dụng giảm giá!')
            else:
                messagebox.showinfo('Information', 'Bạn không là khách hàng thành viên')
        else:
            messagebox.showinfo('Erorr', 'Không thể nhận diện! Vui lòng điều chỉnh mặt vào giữa khung hình')


if __name__ == '__main__':
    rg = FaceRecognition()
    rg.recognition()
