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

Yas = veriler.iloc[:,1:4].values
#Encoder => kategorik(nominal,ordinal) verileri numeric veriye çeviriyor.
ulke= veriler.iloc[:,0:1].values
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
ulke[:,0]=le.fit_transform(ulke[:,0])

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all')
ulke = ohe.fit_transform(ulke).toarray()

c= veriler.iloc[:,-1:].values

le = LabelEncoder()
c[:,0]=le.fit_transform(c[:,0])

ohe = OneHotEncoder(categorical_features='all')
c = ohe.fit_transform(c).toarray()



#Numpy dizilerini DataFrame'e çevirme
sonuc = pd.DataFrame(data=ulke,index=range(22),columns=['fr','tr','usa'])


sonuc2=pd.DataFrame(data=Yas,index=range(22),columns=['boy','kilo','yas'])


cinsiyet = veriler.iloc[:,-1].values

sonuc3=pd.DataFrame(data=c,index=range(22),columns=['cinsiyet'])

#DataFrameleri birleştirme
s=pd.concat([sonuc,sonuc2],axis=1)
print(s)

s2=pd.concat([s,sonuc3],axis=1)
print(s2)



#Makine öğrenmesi algoritması için test ve eğitim verisi ayırma
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33,random_state=0)


#Veriyi normalize etme
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train= sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)
















