import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as pt

eda=pd.read_csv('Titanic Dataset.csv')


sb.countplot(data=eda, x='Gender', hue='Survived')
pt.show()

sb.displot(eda['Age'], kde=False, bins=40)
pt.show()

sb.displot(eda['Fare'])
pt.show()

sb.boxplot(x='Pclass',y='Age',data=eda)
pt.show()
#passngers from which Pclass survived the most and the least?
sb.countplot(data=eda, x='Pclass',hue='Survived', palette='winter')
pt.show()