# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:35:30 2019

@author: hakan
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

veriler = pd.read_csv('odev_tenis.csv')

outlook = veriler.iloc[:,0:1].values
print(outlook)

le = LabelEncoder()
outlook[:,0] = le.fit_transform(outlook[:,0])
print(outlook)

ohe = OneHotEncoder(categorical_features='all')
outlook=ohe.fit_transform(outlook).toarray()
print(outlook)

temp = veriler.iloc[:,1:3].values

wind = veriler.iloc[:,3:4].values
print(wind)
wind[:,0] = le.fit_transform(wind[:,0])

wind=ohe.fit_transform(wind).toarray()
print(wind)

play = veriler.iloc[:,-1:].values
print(play)
play[:,0] = le.fit_transform(play[:,0])

play=ohe.fit_transform(play).toarray()
print(play)


sonuc = pd.DataFrame(data = outlook, index = range(14), columns=['over','rain','sun'] )
print(sonuc)

sonuc2 =pd.DataFrame(data = temp, index = range(14), columns = ['temprature','humidity'])
print(sonuc2)

sonuc3=pd.DataFrame(data=wind[:,0:1],index=range(14),columns=['windy'])
print(sonuc3)

sonuc4=pd.DataFrame(data=play[:,0:1],index=range(14),columns=['play'])
print(sonuc4)

s=pd.concat([sonuc,sonuc2],axis=1)
s2=pd.concat([s,sonuc3],axis=1)
s3=pd.concat([s2,sonuc4],axis=1)

from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(s2,sonuc4,test_size=0.33, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

import statsmodels.formula.api as sm 
X = np.append(arr = np.ones((14,1)).astype(int), values=s2, axis=1 )
X_l = s2.iloc[:,[0,1,2,3,4,5]].values
r_ols = sm.OLS(endog = sonuc4, exog =X_l)
r = r_ols.fit()
print(r.summary())

X_l = s2.iloc[:,[0,4]].values
r_ols = sm.OLS(endog = sonuc4, exog =X_l)
r = r_ols.fit()
print(r.summary())





