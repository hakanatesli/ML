# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:32:47 2019

@author: hakan
"""
#kütüphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#veri yükleme
veriler = pd.read_csv('maaslar.csv')

#data frame dilimleme(slice)
x = veriler.iloc[:,1:2]
y= veriler.iloc[:,2:]

#numPY dizi(array) dönüşümü
X=x.values
Y=y.values

#linear regression
#doğrusal model oluşturma
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X,Y)

#polinomial regression
#doğrusal olmayan model oluşturma
# 2.dereceden polinom
from sklearn.preprocessing import PolynomialFeatures
poly_reg= PolynomialFeatures(degree=2)
x_poly = poly_reg.fit_transform(X)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)

# 4.dereceden polinom
poly_reg3= PolynomialFeatures(degree=4)
x_poly3 = poly_reg3.fit_transform(X)
lin_reg3=LinearRegression()
lin_reg3.fit(x_poly3,y)

# görselleştirme
plt.scatter(X,Y,color='red')
plt.plot(x,lr.predict(X),color='blue')
plt.show()

plt.scatter(X,Y,color = 'red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.show()

plt.scatter(X,Y,color = 'red')
plt.plot(X,lin_reg3.predict(poly_reg3.fit_transform(X)), color = 'blue')
plt.show()

#tahminler
print(lr.predict([[11]]))
print(lr.predict([[6.6]]))

print(lin_reg2.predict(poly_reg.fit_transform([[11]])))
print(lin_reg2.predict(poly_reg.fit_transform([[6.6]])))



