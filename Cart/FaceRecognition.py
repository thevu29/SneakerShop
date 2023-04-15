import cv2
import face_recognition as fr
import numpy as np
import os
from tkinter import messagebox

class FaceRecognition:
    images = []
    faceEncodings = []
    faceNames = []
    knownFacenames = []
    faceDetect = False

    def __init__(self):
        pass

    def loadData(self):
        for item in os.listdir('./img/vip_customer'):
            currentImg = cv2.imread(f'./img/vip_customer/{item}')
            self.images.append(currentImg)
            self.knownFacenames.append(os.path.splitext(item)[0])
        
        for image in self.images:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            try:
                faceEncoding = fr.face_encodings(image)[0]
                self.faceEncodings.append(faceEncoding)
            except:
                pass

    def recognition(self, newName):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            messagebox.showerror('Error', 'Không thể truy cập camera')

        cnt = 0
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
                    self.faceDetect = True
                    name = self.reName(self.knownFacenames[matchesIndex])
                else:
                    self.faceDetect = False
            
            for faceLocation in currentFaceFrame:
                y1, x2, y2, x1 = faceLocation
                y1, x2, y2, x1 = y1 * 2, x2 * 2, y2 * 2, x1 * 2

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
        
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
                if newName == '':
                    messagebox.showerror('Error', 'Vui lòng nhập tên để dùng làm tên lưu ảnh')
                else:
                    self.saveNewVipCustomer(newName)
    
    def saveNewVipCustomer(self, newName):        
        cap = cv2.VideoCapture(0)

        fps = cap.get(cv2.CAP_PROP_FPS)

        cnt = 0
        max = 20
        max_cnt = 0

        while cnt <= 10:
            ret, frame = cap.read()

            if not ret:
                break
            
            if max_cnt < max:
                max_cnt += 1
                continue
            max_cnt = 0
                
            filename = f'./img/vip_customer/{newName} ({cnt}).png'
            cv2.imwrite(filename, frame)
            
            cnt += 1
            
            cv2.imshow('Quá trình lưu ảnh', frame)
            cv2.waitKey(int(1000/fps))
            
            if cv2.waitKey(1) == ord('q'):
                break
            
        cap.release()
        cv2.destroyAllWindows()
    
    def reName(self, name):
        newName = ''
        for item in self.knownFacenames:
            if name in item:
                s = str(item).split(' ')
                newName = ' '.join([newName + s[i] for i in range(0, len(s) - 1)])
                break
    
        return newName
         
# if __name__ == '__main__':
#     f = FaceRecognition()
#     f.loadData()
#     f.recognition('Temp')