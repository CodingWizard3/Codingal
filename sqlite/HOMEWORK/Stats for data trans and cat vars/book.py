#Don't have it imported in terminal
#from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as pt
import seaborn as sb
import pandas as pd
import numpy as np
import statistics as stat

book=pd.read_csv('Bestsellers with categories.csv')
print(book.isnull().sum())

sb.countplot(data=book, x='Genre')
pt.show()
print(book['Genre'].value_counts())
median_G=np.median(book['Genre'])
print('The median Genre is',median_G)

book.groupby('Genre').size().plot(kind='pie', autopct='%2f')
pt.show()
#Nums=book[0:1['User Rating','Reviews','Price','Year']]
#sb.boxplot(x=Nums,palette='winter' )
#pt.show()

#scaler=StandardScaler() 
#standardized_data=scaler.fit_transform(book) 
#standardized_data