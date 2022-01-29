# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 23:43:35 2022

@author: LOUKIK RAINA
"""

import warnings 
warnings.filterwarnings('ignore')
import numpy as np
import cv2
import pickle
from keras.models import load_model
from tensorflow import keras


threshold = 0.90
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX


model = load_model('asl_model')


def preprocessing(img):
    img = img.astype("uint8")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img/255
    return img

alphabet = "abcdefghiklmnopqrstuvwxy"
dictionary = {}
for i in range(24):
    dictionary[i] = alphabet[i]
dictionary

while True:
    sucess, imgOriginal = cap.read()
    img = np.asarray(imgOriginal)
    cv2.rectangle(img, (100,100), (300, 300), (50,50,255), 2)
    crop_img = img[100:300, 100:300]
    img = cv2.resize(crop_img, (28,28))
    img = preprocessing(img)
    img = img.reshape(1, 28, 28, 1)
    cv2.putText(imgOriginal, "Alphabet", (20,35), font, 0.75, (0,0,255), 2, cv2.LINE_AA)
    cv2.putText(imgOriginal, "Probability", (20,75), font, 0.75, (255,0,255), 2, cv2.LINE_AA)
    prediction = model.predict(img)
    predicted_letter = dictionary[np.argmax(prediction)]
    probabilityVal = np.amax(prediction)
    
    if probabilityVal>threshold:
        cv2.putText(imgOriginal, predicted_letter, (150,35), font, 0.75, (0,0,255), 2, cv2.LINE_AA)
        cv2.putText(imgOriginal, str(round(probabilityVal*100,2))+"%", (180,75), font, 0.75, (255,0,255), 2, cv2.LINE_AA)
    cv2.imshow("Result", imgOriginal)
    cv2.imshow("Cropped_img", crop_img)
    k = cv2.waitKey(1)
    if k==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()