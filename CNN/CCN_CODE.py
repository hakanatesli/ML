# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:39:12 2019

@author: hakan
"""

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#ilkleme
classifier = Sequential()

#Adım 1 - Convolution
classifier.add(Convolution2D(32,3,3, input_shape=(64,64,3),activation='relu'))

#Adım 2 - Pooling 
classifier.add(MaxPooling2D(pool_size=(2,2)))

#2.Convolution Katmanı
classifier.add(Convolution2D(32,3,3, input_shape=(64,64,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

#Adım 3 - Flatting
classifier.add(Flatten())

#Adım 4 - YSA
classifier.add(Dense(output_dim=128,activation='relu'))
classifier.add(Dense(output_dim=1,activation='sigmoid'))

#CNN
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#CNN ve fotoğraflar

from keras.preprocessing.image import ImageDataGenerator

training_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen=ImageDataGenerator(rescale=1./255,
                                shear_range=0.2,
                                zoom_range=0.2,
                                horizontal_flip=True)

training_set= training_datagen.flow_from_directory('veriler/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 1,
                                                 class_mode = 'binary')

test_set=test_datagen.flow_from_directory('veriler/test_set',
                                          target_size=(64,64),
                                          batch_size=1,
                                          class_mode='binary')

classifier.fit_generator(training_set,
                         samples_per_epoch = 8000,
                         nb_epoch = 1,
                         validation_data = test_set,
                         nb_val_samples = 2000)

import numpy as np
import pandas as pd

test_set.reset()
pred=classifier.predict_generator(test_set,verbose=1)

pred[pred > .5] = 1
pred[pred <= .5] = 0

print('prediction gecti')
#labels = (training_set.class_indices)

test_labels = []

for i in range(0,int(203)):
    test_labels.extend(np.array(test_set[i][1]))
    
print('test_labels')
print(test_labels)

dosyaisimleri = test_set.filenames
#abc = test_set.
#print(idx)
#test_labels = test_set.
sonuc = pd.DataFrame()
sonuc['dosyaisimleri']= dosyaisimleri
sonuc['tahminler'] = pred
sonuc['test'] = test_labels   

from sklearn.metrics import confusion_matrix


cm = confusion_matrix(test_labels, pred)
print (cm)












