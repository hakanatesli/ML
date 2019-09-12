# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:02:08 2019

@author: hakan
"""

import numpy as np
import pandas as pd
import re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

yorumlar = pd.read_csv('Restaurant_Reviews.csv')
nltk.download('stopwords')

ps=PorterStemmer()

derlem = []
for i in range(1000):
    yorum=re.sub('[^a-zA-Z]',' ',yorumlar['Review'][i])
    yorum = yorum.lower()
    yorum= yorum.split()
    yorum =[ ps.stem(kelime) for kelime in yorum if not kelime in set(stopwords.words('english')) ]
    yorum = ' '.join(yorum)
    derlem.append(yorum)


cv = CountVectorizer(max_features=2000)
X = cv.fit_transform(derlem).toarray() #bağımsız değişken
y = yorumlar.iloc[:,1].values #bağımlı değişken

X_train, X_test , y_train , y_test = train_test_split(X,y,test_size=0.20,random_state = 0)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train,y_train)
y_pred = gnb.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)

print(cm)
