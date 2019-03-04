#polynomial regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, 2].values

#fitting linear regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

#fitting polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, y)

#visualising the linear regression results
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('truth or bluff (linear regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()

#visualising the polynomial regresesion results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))

plt.scatter(X, y, color='red')
plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)), color='blue')
plt.title('truth or bluff (polynomial regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()

#predicting a new result with linear regression
lin_reg.predict(np.array(6.5).reshape(1, -1))

#predicting a new result with polynomial regression
lin_reg2.predict(poly_reg.fit_transform(np.array(6.5).reshape(1, -1)))