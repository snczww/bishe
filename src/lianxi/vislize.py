#!/usr/bin/env python

# encoding: utf-8

'''

@author: zww

@contact: snczww@gmail.com

@software: 2017/12/10 12:36

@file: vislize.py

@time: 2017/12/10 12:36

@desc:


'''
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

# Read data from a csv
z_data = pd.read_csv('data\zcdata.csv')

data = [
    go.Surface(
        z=z_data.as_matrix()
    )
]
layout = go.Layout(
    title='Mt Bruno Elevation',
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='elevations-3d-surface')