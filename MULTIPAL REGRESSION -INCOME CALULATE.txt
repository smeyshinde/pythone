import pandas as pd
import numpy as np
from sklearn import linear_model

df = pandas.read_csv("multiple_linear_regression_dataset.csv")
print(df)
df.hist()

X=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

regr = linear_model.LinearRegression()
regr.fit(X, y)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,y_train)
y_pred=reg.predict(X_test)
print(y_pred)

np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))
from sklearn.metrics import mean_squared_error,mean_squared_error
mean_squared_error(y_test, y_pred)

#predict the Salary of Employe where the age is 23 and experence is of 3:
predictedSalary = regr.predict([[21, 0]])

print(predictedSalary)
