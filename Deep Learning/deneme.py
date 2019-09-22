# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:04:01 2019

@author: hakan
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

veriler = pd.read_csv('Churn_Modelling.csv')

X = veriler.iloc[:,3:13].values
Y=veriler.iloc[:,13].values

from sklearn.preprocessing import LaberEncoder
le=LaberEncoder()
X[:,1]=le.fit_transform(veriler.iloc[:,1])

le2=LaberEncoder()
X[:,2]=le2.fit_transform(veriler.iloc[:,2])


from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features=[1])
X=ohe.fit_transform(X).toarray()
X=X[:,1:]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.33,random_state=0)

from sklearn.preprocessing import StandartScaler
sc=StandartScaler()
X_test=sc.fit_transform(x_test)
X_train=sc.fit_transform(x_train)

import keras 
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

classifier.add(Dense(6,init='uniform',activation='relu',input_dim=11))

classifier.add(Dense(6,init='uniform',activation='relu'))

classifier.add(Dense(1,init='uniform',activation='sigmoid'))

classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

classifier.fit(X_train,y_train,epocs=50)

y_pred=classifier.predict(X_test)

y_pred =(y_pred>0.5)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test,y_pred)

print(cm)




