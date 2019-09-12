# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:52:01 2019

@author: hakan
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

#Random Selection(Rastegele Seçim)
'''
import random

N=10000     #verimizdeki satır sayısı
d=10    #verimizdeki sütun sayısı
toplam=0    #ödül ceza sistemindeki ödülleri toplayacak değişken
secilenler=[]   #n.satıda secilen random sütun sayısını ulundurucak dizi
for n in range(0,N):    
    ad=random.randrange(d)  #1'den 10'a kadar bi sayı üretiyor.
    secilenler.append(ad)   #üretilen sayıyı secilenler dizisine atıyor.
    odul=veriler.values[n,ad]   #Eğer n.satıdaki ad.sütun seçilen reklamsa 1 değilse 0 dönüyor.
    toplam=toplam+odul   #ödüller toplanıyor.
    
plt.hist(secilenler)
plt.show()
'''

#Thompson Algorithm
import random

N=10000     #verimizdeki satır sayısı
d=10    #verimizdeki sütun sayısı

toplam=0    #ödül ceza sistemindeki ödülleri toplayacak değişken
secilenler=[]   #n.satıda secilen random sütun sayısını bulundurucak dizi

birler=[0]*d
sifirlar=[0]*d
for n in range(1,N):    #her satırı dönecek olan döngü
    ad=0 #secilen ilan
    max_th=0
    for i in range(0,d):    #her sütunu dönecek olan döngü
        rasbeta=random.betavariate(birler[i]+1,sifirlar[i]+1)
        if rasbeta>max_th:
            max_th = rasbeta
            ad=i
    secilenler.append(ad)   #üretilen sayıyı secilenler dizisine atıyor.
    odul=veriler.values[n,ad]   #Eğer n.satıdaki ad.sütun seçilen reklamsa 1 değilse 0 dönüyor.
    if odul==1:
        birler[ad]=birler[ad]+1
    else:
        sifirlar[ad]=sifirlar[ad]+1
    toplam=toplam+odul   #ödüller toplanıyor.
    
print('Toplam odul:')
print(toplam)

plt.hist(secilenler)
plt.show()

