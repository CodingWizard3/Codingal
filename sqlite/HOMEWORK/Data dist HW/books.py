import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

book=pd.read_csv('Bestsellers with categories.csv')
print(book.isnull().sum())

var_user = np.var(book['User Rating']) 
print("Variation of the user rating is:", var_user) 
standard_deviation_user = np.std(book['User Rating'])
print("Standard Deviation of the User Rating is", standard_deviation_user)

var_price = np.var(book['Price']) 
print("Variation of the Price is:", var_price) 
standard_deviation_price = np.std(book['Price'])
print("Standard Deviation of the Price is", standard_deviation_price)

pt.hist(book['User Rating'],bins=[4.0,4.2,4.4,4.6,4.8,5.0])
pt.ylabel('Price')
pt.xlabel('User Rating')
pt.show()

pt.hist(book['Price'],bins=[0,5,10,15,20,25,30,35,40,45,50])
pt.xlabel('Price')
pt.ylabel('User Rating')
pt.show()