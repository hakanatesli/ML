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
veriler = pd.read_csv("veriler.csv")

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
