import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error,r2_score

x,y = datasets.load_diabetes(return_X_y=True)
print(x)
print(y)

x=x[:,np.newaxis,2]
x_train=x[:-20]
x_test=x[-20:]
y_train=y[:-20]
y_test=y[-20:]
print(x_train.shape)
print(y_train.shape)

regr = linear_model.LinearRegression()
regr.fit(x_train,y_train)
y_pred=regr.predict(x_test)

print('coefficients',regr.coef_)
print('mean squared error: %.2f'%mean_squared_error(y_test,y_pred))
print('coefficient of determination %.2f' %r2_score(y_test,y_pred))

plt.scatter(x_test,y_test,color='black')
plt.plot(x_test,y_pred,color='blue',linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()