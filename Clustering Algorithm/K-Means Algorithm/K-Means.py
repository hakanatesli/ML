# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:19:45 2019

@author: hakan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('musteriler.csv')

X= veriler.iloc[:,3:].values

from sklearn.cluster import KMeans 

kmeans = KMeans(n_clusters = 3, init= 'k-means++')

kmeans.fit(X)

print(kmeans.cluster_centers_)

sonuclar =[]

for i in range(1,10):
    kmeans = KMeans(n_clusters = i, init= 'k-means++', random_state=123)
    kmeans.fit(X)
    sonuclar.append(kmeans.inertia_)
    
plt.plot(range(1,10),sonuclar)