#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from keras.models import load_model
import cv2
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from time import sleep


# In[2]:


face_classifier = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
classifier =load_model(r'model.h5')

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_classifier.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)



        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

            prediction = classifier.predict(roi)[0]
            label=emotion_labels[prediction.argmax()]
            label_position = (x,y-10)
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        else:
            cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow('Emotion Detector',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# prediction output
# 

# In[3]:


print (prediction)
print(label)


# In[4]:


if (label=='Neutral'):
    print("play some normal music")
elif(label=='Sad'):
    print("play some sad songs")
elif(label=='Happy'):
    print("hi")


# In[ ]:





# pip install pydub

# In[ ]:


from pydub import AudioSegment
from pydub.playback import play
import random
neutrals = ['neutral1.m4a','neutral2.m4a','neutral3.m4a']
happies = ['happy1.m4a','happy2.m4a','happy3.m4a']
angrys = []
disgusts = []
surprises = []
fears = []
sads=['sad1.m4a','sad3.m4a','sad2.m4a']
i = 0
# Input an existing wav filename

#for Neutral
if(label=="Neutral"):
    for i in range(0,len(neutrals)):
        wavFile =neutrals[i]
        sound = AudioSegment.from_file(wavFile)
        print("Playing wav file...")
    # play the fileagh
        while True:
            try:
                play(sound)
            except KeyboardInterrupt:
                print ("Stopping playing")
                break
    
    
elif(label=="Sad"):
    for i in range(0,len(sads)):
        wavFile =sads[i]
        sound = AudioSegment.from_file(wavFile)
        print("Playing wav file...")
    # play the fileagh
        while True:
            try:
                play(sound)
            except KeyboardInterrupt:
                print ("Stopping playing")
                break
    
    
    
elif(label=="Fear"):
    for i in range(0,len(fears)):
        wavFile =fears[i]
        sound = AudioSegment.from_file(wavFile)
        print("Playing wav file...")
    # play the fileagh
        while True:
            try:
                play(sound)
            except KeyboardInterrupt:
                print ("Stopping playing")
                break
    
    
    
elif(label=="Happy"):
    for i in range(0,len(happies)):
        wavFile =happies[i]
        sound = AudioSegment.from_file(wavFile)
        print("Playing wav file...")
    # play the fileagh
        while True:
            try:
                play(sound)
            except KeyboardInterrupt:
                print ("Stopping playing")
                break
    
    
    
elif(label=="Angry"):
    for i in range(0,len(angries)):
        wavFile =angries[i]
        sound = AudioSegment.from_file(wavFile)
        print("Playing wav file...")
    # play the fileagh
        while True:
            try:
                play(sound)
            except KeyboardInterrupt:
                print ("Stopping playing")
                break
    
    
    
elif(label=="Surprise"):
    for i in range(0,len(surprises)):
        wavFile =surprises[i]
        sound = AudioSegment.from_file(wavFile)
        print("Playing wav file...")
    # play the fileagh
        while True:
            try:
                play(sound)
            except KeyboardInterrupt:
                print ("Stopping playing")
                break
    
    
    
elif(label=="Disgust"):
    for i in range(0,len(disgust)):
        wavFile =disgust[i]
        sound = AudioSegment.from_file(wavFile)
        print("Playing wav file...")
    # play the fileagh
        while True:
            try:
                play(sound)
            except KeyboardInterrupt:
                print ("Stopping playing")
                playback.stop()  
                break


# In[ ]:




    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




