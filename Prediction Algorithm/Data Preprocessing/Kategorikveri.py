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

print(veriler)


boy= veriler[['boy']]
boykilo=veriler[['boy','kilo']]

print(boykilo)
print(boy)

var1=10
#
degisken="günaydın"

class insan:
    boy=180
    def kosmak(self,x):
        return x + 10
    
ali =insan()
print(ali.boy)
print(ali.kosmak(80))

#eksik veriler

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values="NaN",strategy= 'mean', axis=0 )

Yas = veriler.iloc[:,1:4].values

print(Yas)

imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4]=imputer.transform(Yas[:,1:4])

print(Yas)


Ulke= veriler.iloc[:,0:1].values
print(Ulke)


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le = LabelEncoder()

Ulke[:,0]=le.fit_transform(Ulke[:,0])

print(Ulke)


ohe = OneHotEncoder(categorical_features='all')

Ulke = ohe.fit_transform(Ulke).toarray()
print(Ulke)







