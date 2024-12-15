import pandas as pd
import statistics as stats
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sb

book=pd.read_csv('Bestsellers with categories.csv')
print(book.isnull().sum())

price10=np.quantile(book['Price'],0.10)
print(price10,'is 10% of the feature price')

price_q1=np.quantile(book['Price'],0.25)
price_q2=np.quantile(book['Price'],0.50)
price_q3=np.quantile(book['Price'],0.75)

print('Q1 is',price_q1)
print('Q2 is',price_q2)
print('Q3 is',price_q3) 

sb.boxplot(data=book ,x='Price',hue='User Rating', palette='winter')
pt.show()