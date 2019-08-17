# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#kodlar

#veri yükleme
veriler = pd.read_csv("eksikveriler.csv")


boy= veriler[['boy']]
boykilo=veriler[['boy','kilo']]


var1=10
#
degisken="günaydın"

class insan:
    boy=180
    def kosmak(self,x):
        return x + 10
    
ali =insan()

#eksik veriler

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values="NaN",strategy= 'mean', axis=0 )

Yas = veriler.iloc[:,1:4].values

imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4]=imputer.transform(Yas[:,1:4])

Ulke= veriler.iloc[:,0:1].values


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
Ulke[:,0]=le.fit_transform(Ulke[:,0])

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all')
Ulke = ohe.fit_transform(Ulke).toarray()

sonuc = pd.DataFrame(data=Ulke,index=range(22),columns=['fr','tr','usa'])

print(sonuc)

sonuc2=pd.DataFrame(data=Yas,index=range(22),columns=['boy','kilo','yas'])

print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values

sonuc3=pd.DataFrame(data=cinsiyet,index=range(22),columns=['cinsiyet'])

s=pd.concat([sonuc,sonuc2],axis=1)
print(s)

s2=pd.concat([s,sonuc3],axis=1)
print(s2)


#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33,random_state=0)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train= sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)
















