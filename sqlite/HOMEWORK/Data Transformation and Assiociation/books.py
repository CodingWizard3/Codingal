import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sb

book=pd.read_csv('Bestsellers with categories.csv')
print(book.isnull().sum())
print(book.info())
bins=[0,50,100]
rating_labels=['Good', 'Excellent']
book['binned rating']=pd.cut(book['User Rating'], bins, labels=rating_labels)

sb.distplot(book['Price'])
pt.show()
print('Skewness -', book['Price'])

sb.boxplot(data=book, x='Genre',y='User Rating')
pt.show()

sb.boxplot(data=book, x='Price',y='User Rating')
pt.show()