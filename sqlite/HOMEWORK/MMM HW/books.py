import statistics as stats
import pandas as pd
import numpy as np

book = pd.read_csv('Bestsellers with categories.csv')
print(book.isnull().sum())

print('USER RATING')
meanUser=np.mean(book['User Rating'])
print('The average user rating is',meanUser) 
modeUser=stats.mode(np.array(book['User Rating']))
print('The most frequent user rating is',modeUser) 
medianUser=np.median(book['User Rating'])
print('The median user rating is',medianUser) 


print('PRICE')
meanPrice=np.mean(book['Price'])
print('The average price is',meanPrice)
modePrice=stats.mode(np.array(book['Price']))
print('The most frequent price is',modePrice) 
medianPrice=np.median(book['Price'])
print('The median price is',medianPrice) 


print('REVIEWS')
meanRev=np.mean(book['Reviews'])
print('The average amount of reviews are',meanRev)
modeRev=stats.mode(np.array(book['Reviews']))
print('The most frequent reviews are',modeRev) 
medianRev=np.median(book['Reviews'])
print('The median amount of reviews are',medianRev) 