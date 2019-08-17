# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.Veri Ön işleme

#2.1 Veri Yükleme
veriler = pd.read_csv("veriler.csv")

x = veriler.iloc[:,2:3].values #bağımsız değişkenler
y = veriler.iloc[:,4:].values #bağımlı değişkenler

#Makine öğrenmesi algoritması için test ve eğitim verisi ayırma
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33,random_state=0)


#Veriyi normalize etme
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train= sc.fit_transform(x_train)
X_test=sc.transform(x_test)

from sklearn.linear_model import LogisticRegression
logr=LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

y_pred = logr.predict(X_test)
print(y_pred)
print(y_test)


from sklearn.metrics import confusion_metrix

cm=confuion_metrix(y_test,y_pred)
print(cm)



















