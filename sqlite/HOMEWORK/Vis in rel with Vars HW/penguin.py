import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sb

penguin=pd.read_csv('Penguins Data.csv')

pt.scatter(data=penguin, x='Culmen Length (mm)',y='Body Mass (g)')
pt.show()
pt.scatter(data=penguin, x='Culmen Depth (mm)',y='Body Mass (g)')
pt.show()
sb.pairplot(data=penguin)
pt.show()
#4  Area chart: dist? Line?
sb.displot(data=penguin,x='Culmen Length (mm)',y='Body Mass (g)')
pt.show()
sb.lineplot(data=penguin,x='Culmen Length (mm)',y='Body Mass (g)')
pt.show()