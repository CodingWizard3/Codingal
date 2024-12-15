
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as pt
import seaborn as sb
import pandas as pd
import numpy as np
import statistics as stat

book=pd.read_csv('C:/Users/Shruthi Mekala/Desktop/Python-MK/Codingal/sqlite/HOMEWORK/Stats for data trans and cat vars/Bestsellers with categories.csv')
print(book.isnull().sum())

sb.countplot(data=book, x='Genre')
pt.show()

G_cat=['Non Fiction','Fiction']
book['B']=pd.Categorical(book['Genre'],G_cat, ordered=True)
book2=pd.DataFrame(book['B'])
print(book2.head())

print(book.head())

#book2.groupby().size().plot(kind='pie', autopct='%2f')
#pt.show()

sb.boxplot(data=book2,x='B',hue='B',palette='winter' )
pt.show()

scaler=StandardScaler() 
standardized_data=scaler.fit_transform(book2) 
print(standardized_data)