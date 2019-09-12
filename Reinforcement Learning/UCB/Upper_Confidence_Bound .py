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


#Upper Confidence Bound(Üst Güven Sınırı)

import math

N=10000     #verimizdeki satır sayısı
d=10    #verimizdeki sütun sayısı

oduller=[0]* d   #Ri(n) --> O ana kadarki i reklamından gelen ödül
tiklamalar=[0]*d   #Ni(n) --> i sayılı reklamın o ana kadarki tıklama sayısı
toplam=0    #ödül ceza sistemindeki ödülleri toplayacak değişken
secilenler=[]   #n.satıda secilen random sütun sayısını bulundurucak dizi

for n in range(1,N):    #her satırı dönecek olan döngü
    ad=0 #secilen ilan
    max_ucb=0
    for i in range(0,d):    #her sütunu dönecek olan döngü
        if(tiklamalar[i]>0):    #ilk satıda değilse aşağıdaki değişkenşeri buluyor.
            ortalama=oduller[i]/tiklamalar[i]
            delta=math.sqrt(3/2*math.log(n)/tiklamalar[i])
            ucb=ortalama+delta
        else:   #ilk satır için yazılmış kontrol.
            ucb=N*10
        if(max_ucb<ucb):    #her satır için max_ucb değeri bulunuyor.
            max_ucb=ucb
            ad=i
    secilenler.append(ad)   #üretilen sayıyı secilenler dizisine atıyor.
    tiklamalar[ad]=tiklamalar[ad]+1
    odul=veriler.values[n,ad]   #Eğer n.satıdaki ad.sütun seçilen reklamsa 1 değilse 0 dönüyor.
    oduller[ad]=oduller[ad]+odul
    toplam=toplam+odul   #ödüller toplanıyor.
    
print('Toplam odul:')
print(toplam)

plt.hist(secilenler)
plt.show()











