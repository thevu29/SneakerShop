import cv2
import os
import numpy as np
from PIL import Image

class Train:
    def __init__(self):
        self.path = './img/vip_customer'
        self.detector = cv2.CascadeClassifier('./FaceRecognition/haarcascade_frontalface_default.xml')
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    def training(self, name):
        imagePath = os.path.join(self.path, name)
        faceSamples = []
        ids = []
        
        for i in range(1, 31):
            PIL_img = Image.open(f'{imagePath} ({i}).png').convert('L')
            img_numpy = np.array(PIL_img, 'uint8')

            path = os.path.split(f'{imagePath} ({i}).png')[-1].split('.')[0].split(' ')
            id = int(path[len(path) - 1].lstrip('(').rstrip(')'))
            faces = self.detector.detectMultiScale(img_numpy)
            
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y+h, x:x+w])
                ids.append(id)
        
        self.recognizer.train(faceSamples, np.array(ids))
        self.recognizer.write(f'./Classifiers/{name}.xml')