# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:32:47 2019

@author: hakan
"""
#veri yukleme
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv('maaslar.csv')

x = veriler.iloc[:,1:2]
y= veriler.iloc[:,2:]
X=x.values
Y=y.values

#linear regression
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X,Y)

plt.scatter(X,Y,color='red')
plt.plot(x,lr.predict(X),color='blue')
plt.show()

#polinomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg= PolynomialFeatures(degree=2)
x_poly = poly_reg.fit_transform(X)
print(x_poly)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(X,Y,color = 'red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.show()


from sklearn.preprocessing import PolynomialFeatures
poly_reg= PolynomialFeatures(degree=4)
x_poly = poly_reg.fit_transform(X)
print(x_poly)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(X,Y,color = 'red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.show()

#tahminler
print(lr.predict([[11]]))
print(lr.predict([[6.6]]))

print(lin_reg2.predict(poly_reg.fit_transform([[11]])))
print(lin_reg2.predict(poly_reg.fit_transform([[6.6]])))

