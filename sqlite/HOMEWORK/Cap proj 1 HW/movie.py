import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sb

movie=pd.read_csv('IMDB Dataset.csv')
print(movie.head(3))
print(movie.tail(3))
print(movie.info())
print(movie.isnull().sum())
prime=movie.loc[41:75]  
sb.boxplot(data=prime,x='IMDB_Rating',y='Runtime')
pt.show()
sb.pairplot(data=prime)
pt.show()
sb.displot(data=prime,x='IMDB_Rating',y='Runtime')
pt.show()
sb.countplot(data=prime,y='IMDB_Rating')
pt.show()