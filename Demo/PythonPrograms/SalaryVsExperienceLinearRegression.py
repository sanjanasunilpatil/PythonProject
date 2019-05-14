# importing Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

# Importing data-set
dataSet = pd.read_csv('../inputFiles/Salary_Data.csv')
x = dataSet.iloc[:, 0:-1]
y = dataSet.iloc[:, -1:0:-1]

# Checking for null values
if dataSet['Salary'].isnull().sum() > 0:
    print("Null values are present")
else:
    print("Null values are not present")

# Splitting data-set into training and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3)

# Fitting training set
regression = LinearRegression()
regression.fit(x_train, y_train)

# Predicting test set
y_pred = regression.predict(x_test)

# Plotting training set result into graphs
plt.scatter(x_train, y_train, c='r')
plt.plot(x_train, regression.predict(x_train), c='b')
plt.title("Experience Vs Salary for training set")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

# Plotting test set result into graphs
plt.scatter(x_test, y_test, c='r')
plt.plot(x_train, regression.predict(x_train), c='b')
plt.title("Experience Vs Salary for test set")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()
