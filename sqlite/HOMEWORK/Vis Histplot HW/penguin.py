import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

penguin=pd.read_csv('Penguins Data.csv')
pt.hist(penguin['Culmen Length (mm)'],bins=[30,35,40,45,50,55,60],color='brown')
pt.show()

pt.hist(penguin['Culmen Depth (mm)'],bins=[13,14,15,16,17,18,19,20,21,22],color='green')
pt.show()

pt.hist(penguin['Flipper Length (mm)'],bins=[170,175,180,185,190,195,200,205,210,215,220,225,230,235,240],color='purple')
pt.show()

pt.hist(penguin['Body Mass (g)'],bins=[2500,3000,3500,4000,4500,5000,5500,6000,6500],color='orange')
pt.show()