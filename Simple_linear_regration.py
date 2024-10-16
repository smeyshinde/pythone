import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
dataset = pd.read_csv('score.csv')

# Extract features (all columns except the last one)
x = dataset.iloc[:, :-1]

# Extract target variable (the last column)
y = dataset.iloc[:, -1]

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(x_test)

# Visualising the Training set results
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'cyan')
plt.title('Study Hours vs Score (Training set)')
plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.show()

# Visualising the Test set results
plt.scatter(x_test, y_test, color = 'cyan')
plt.plot(x_train, regressor.predict(x_train), color = 'yellow')
plt.title('Study Hours vs Score (Test set)')
plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.show()
