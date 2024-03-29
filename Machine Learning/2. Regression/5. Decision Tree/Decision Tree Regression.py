# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the Dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# Fitting the Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor(random_state= 0)
reg.fit(X, y)


# Predicting a new Result
y_pred = reg.predict(6.5)


# Visualizing the Decision Tree Regression results ( for higher resolution and smoother curve)
X_grid = np.arange(min(X),max(X), 0.1 )
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, reg.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff using Decision Tree Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
