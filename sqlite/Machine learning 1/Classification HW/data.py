from numpy import where
from collections import Counter
import seaborn as sb
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import pandas as pd

titanic=pd.read_csv('titanic.csv')
print(titanic.shape)
print(titanic.isnull().sum())
print(titanic.head())
titanic.dropna(inplace=True)
sb.heatmap(titanic.isnull(), cbar=False)

pd.get_dummies(titanic['sex']).head()
sex=pd.get_dummies(titanic['sex'], drop_first=True)

pd.get_dummies(titanic['Pclass']).head()
pclass=pd.get_dummies(titanic['Pclass'], drop_first=True)

