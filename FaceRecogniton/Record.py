import cv2
from threading import Thread
from time import sleep
from tkinter import messagebox

try:
    from .Train import *
except:
    from Train import *

class Record:
    def __init__(self, customerName):
        self.customerName = customerName
        
    def saveImage(self):
        cv2.imwrite(f'./img/vip_customer/{self.customerName} ({self.cnt}).png', self.roi_color)
        self.cnt += 1
        sleep(1)
        
    def recording(self):
        face_cascade = cv2.CascadeClassifier('./FaceRecognition/haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        
        self.cnt = 1
        while (True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                self.roi_color = frame[y:y+h, x:x+w]

                if self.cnt < 45:
                    if self.cnt == 1:
                        messagebox.showinfo('Thông báo', 'Vui lòng nhìn thẳng')
                    if self.cnt == 15:
                        messagebox.showinfo('Thông báo', 'Vui lòng quay sang trái')
                    if self.cnt == 30:
                        messagebox.showinfo('Thông báo', 'Vui lòng quay sang phải')
                        
                    thread = Thread(target=self.saveImage)
                    thread.start()

            if self.cnt == 45:
                messagebox.showinfo('Thông báo', 'Đăng ký khách hàng thành viên thành công')
                break
            
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
            
        cap.release()
        cv2.destroyAllWindows()

        Train().training(self.customerName)