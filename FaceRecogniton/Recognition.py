import cv2
import face_recognition as fr
import numpy as np
import os
import time
from tkinter import messagebox

try:
    from .Record import *
except:
    from Record import *

class FaceRecognition:
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_COMPLEX
        self.face_cascade = cv2.CascadeClassifier('./FaceRecognition/haarcascade_frontalface_default.xml')
        self.training_dir = './Classifiers'
        self.models = {}
        self.faceDetect = False

    def recognizing(self, newName):
        for filename in os.listdir(self.training_dir):
            customerID = filename.split('.')[0]
            self.models[customerID] = cv2.face.LBPHFaceRecognizer_create()
            self.models[customerID].read(os.path.join(self.training_dir, filename))
        
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            messagebox.showerror('Error', 'Không thể truy cập camera')

        cnt = 0
        start_time = time.time()
        while time.time() - start_time < 20:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                customerID = ''
                minimum = 100
                confidences = []
                
                for model_id, model in self.models.items():
                    label, confidence = model.predict(roi_gray)
                    confidences.append(confidence)
                    
                    if confidence < 50 and confidence < minimum:
                        customerID = model_id

                if customerID != '':
                    customerID = self.reName(str(customerID))
                    cv2.putText(frame, str(customerID), (x + 5, y + h + 30), self.font, 1, (255, 0, 255), 2)
                    self.faceDetect = True
                else:
                    cv2.putText(frame, 'unknown', (x + 5, y + h + 30), self.font, 1, (255, 0, 255), 2)
                    self.faceDetect = False
                
            cnt += 1
            cv2.imshow('Quá trình nhận diện', frame)
            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        if self.faceDetect == True:
            messagebox.showinfo('Information', 'Bạn là khách hàng thành viên và được áp dụng giảm giá!')
        else:
            res = messagebox.askyesno('Question', 'Bạn không là khách hàng thành viên \n Bạn có muốn trở thành khách hàng thành viên để được áp dụng giảm giá cho lần đặt mua tiếp theo ?')
            
            if res:
                Record(newName).recording()
        
    def reName(self, name):
        newName = ''
        for item in os.listdir('./img/vip_customer'):
            item = item.split('.')[0]
            tmp = item.replace(' ', '')
            if name.lower() in tmp.lower():
                item = item.split(' ')
                newName = ' '.join([newName + item[i] for i in range(0, len(item) - 1)])
                break
        return newName
            
         
if __name__ == '__main__':
    f = FaceRecognition()
    f.recognizing('Temp')
    # print(f.reName('hainam'))