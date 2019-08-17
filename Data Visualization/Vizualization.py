# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:54:49 2019

@author: hakan
"""
import pandas as pd
import numpy as np

timesData = pd.read_csv("timesData.csv")

timesData.info()

print(timesData.head(10))

df = timesData.iloc[:100,:]

import plotly.plotly as pl
import plotly.graph_objs as go

# Creating trace1
trace1 = go.Scatter(
                    x = df.world_rank,
                    y = df.citations,
                    mode = "lines",
                    name = "citations",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    text= df.university_name)
# Creating trace2
trace2 = go.Scatter(
                    x = df.world_rank,
                    y = df.teaching,
                    mode = "lines+markers",
                    name = "teaching",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'),
                    text= df.university_name)
data = [trace1, trace2]
pl.iplot(data)