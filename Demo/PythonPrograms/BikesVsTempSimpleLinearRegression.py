# Importing libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from matplotlib import pyplot as plt

# Importing dataSet and splitting dataSet into 2 csv files
dataSet = pd.read_csv('../inputFiles/bike_sharing.csv')
df_training = dataSet.sample(frac=0.8)
df_test = pd.concat([dataSet, df_training]).drop_duplicates(keep=False)

df_training.to_csv('../inputFiles/training_data.csv', header=True, index=None)
df_test.to_csv('../inputFiles/test_data.csv', header=True, index=None)

dataSet = pd.read_csv('../inputFiles/training_data.csv')
x_index = dataSet.columns.get_loc("temp")
y_index = dataSet.columns.get_loc("cnt")
x = dataSet.iloc[:, x_index:(x_index+1)]
y = dataSet.iloc[:, y_index:(y_index+1)]

# Checking for null values
if x['temp'].isnull().sum() > 0:
    print("Taking care of null values of temp column")
    x = x.fillna(x.mean())
if y['cnt'].isnull().sum() > 0:
    print("Taking care of null values of cnt column")
    y = y.fillna(y.mean())
else:
    print("Null values are not present")

# Feature Scaling
sc_x = StandardScaler()
x = sc_x.fit_transform(x)

# Splitting data set into training and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape)
print(x_test.shape)

# Fitting training set into linear model
regression = LinearRegression()
regression.fit(x_train, y_train)

# Predicting values
y_pred = regression.predict(x_test)

# Finding accuracy using r2_score
accuracy = r2_score(y_test, y_pred)
print("Accuracy ", accuracy)

# # Plotting graph for training set
# plt.scatter(x_train, y_train, c='r')
# plt.plot(x_train, regression.predict(x_train), c='b')
# plt.title("Temperature Vs Bikes for training set")
# plt.xlabel("Temperature")
# plt.ylabel("Bikes")
# plt.show()
#
# # Plotting graph for test set
# plt.scatter(x_test, y_test, c='r')
# plt.plot(x_train, regression.predict(x_train), c='b')
# plt.title("Temperature Vs Bikes for test set")
# plt.xlabel("Temperature")
# plt.ylabel("Bikes")
# plt.show()
