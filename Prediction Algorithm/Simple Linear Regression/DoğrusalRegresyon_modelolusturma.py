# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:38:38 2019

@author: hakan
"""

#1.kütüphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.Veri YÜkleme
veriler = pd.read_csv('satislar.csv')

#ver ön işleme
aylar=veriler[['Aylar']]
satislar=veriler[['Satislar']]

#Test ve Eğitim kümelerine ayırma

from sklearn.model_selection import train_test_split
#train_test_split fonksiyonunda parametre olarak x sütununu sonra y sütununu veriyosun.
#test_size parametresi test kümesinin oranıdır.
#random_state veriyi sıra ile seçmemesi ile ilgili parametre.
x_train,x_test,y_train,y_test=train_test_split(aylar,satislar,test_size=0.33,random_state=0)

#Verilerin Ölçeklenmesi
from sklearn.preprocessing import StandardScaler

#Veriyi Normalize ediyoruz. 1 0 arasına indirgiiyoruz.
sc=StandardScaler()
X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)
Y_train=sc.fit_transform(y_train)
Y_test=sc.fit_transform(y_test)

#Model inşası
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,Y_train)

