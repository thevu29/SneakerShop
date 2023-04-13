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
        print(len(self.faceEncodings))
        
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
        
        while True:
            ret, frame = cap.read()
            myFrame = cv2.resize(frame, (0, 0), None, fx=0.5, fy=0.5)
            myFrame = cv2.cvtColor(myFrame, cv2.COLOR_BGR2RGB)
            
            currentFaceFrame = fr.face_locations(myFrame)
            currentEncodeFrame = fr.face_encodings(myFrame)
            
            for encodeFace, faceLocation in zip(currentEncodeFrame, currentFaceFrame):
                faceDis = fr.face_distance(self.faceEncodings, encodeFace)
                matchesIndex = np.argmin(faceDis)
                
                if faceDis[matchesIndex] < 0.35:
                    name = self.knownFacenames[matchesIndex]       
                else:
                    name = 'Unknown'
                    
                y1, x2, y2, x1 = faceLocation 
                y1, x2, y2, x1 = y1 * 2, x2 * 2, y2 * 2, x1 * 2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, name, (x2, y2), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) == ord('q'):
                break
            
        cap.release()
        cv2.destroyAllWindows()
        
if __name__ == '__main__':
    rg = FaceRecognition()
    rg.recognition()