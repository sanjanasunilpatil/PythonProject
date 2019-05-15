# importing Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle

# Importing data-set and converting into two csv Files
dataSet = pd.read_csv('../inputFiles/Salary_Data.csv')
df_training = dataSet.sample(frac=0.8)
df_test = pd.concat([dataSet, df_training]).drop_duplicates(keep=False)

df_training.to_csv('../inputFiles/training_data.csv', header=True, index=None)
df_test.to_csv('../inputFiles/test_data.csv', header=True, index=None)

dataSet = pd.read_csv('../inputFiles/training_data.csv')

x_index = dataSet.columns.get_loc("YearsExperience")
y_index = dataSet.columns.get_loc("Salary")

x = dataSet.iloc[:, x_index:(x_index+1)]
y = dataSet.iloc[:, y_index:(y_index+1)]

# Checking for null values
if dataSet['Salary'].isnull().sum() > 0:
    print("Taking care of null values of temp column")
    x = x.fillna(x.mean())

if dataSet['YearsExperience'].isnull().sum() > 0:
    print("Taking care of null values of cnt column")
    y = y.fillna(y.mean())

else:
    print("Null values are not present")

# Splitting data-set into training and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Fitting training set
regression = LinearRegression()
regression.fit(x_train, y_train)

# Predicting test set
y_pred = regression.predict(x_test)

# Calculating accuracy of model
accuracy = r2_score(y_test, y_pred)
print("Accuracy of model ", accuracy)

# Creating and saving pickle model
pkl_fileName = '../inputFiles/LinearRegression.pkl'
linearRegressionPklModel = open(pkl_fileName, 'wb')
pickle.dump(regression, linearRegressionPklModel)
linearRegressionPklModel.close()

# Loading pickle model to predict y data from test_data.csv
linearRegressionPklModel = open(pkl_fileName, 'rb')
regressionModelPkl = pickle.load(linearRegressionPklModel)

# Use pickle's regression model to Predict y values and ca;cu;ate Accuracy
dataSet_testData = pd.read_csv('../inputFiles/test_data.csv')
x_testData = dataSet_testData.iloc[:, x_index:(x_index+1)]
y_testData = dataSet_testData.iloc[:, y_index:(y_index+1)]
y_pred_pkl = regressionModelPkl.predict(x_testData)

accuracy_pk = r2_score(y_testData, y_pred_pkl)

print("Accuracy by pickle model ", accuracy_pk)

# # Plotting training set result into graphs
# plt.scatter(x_train, y_train, c='r')
# plt.plot(x_train, regression.predict(x_train), c='b')
# plt.title("Experience Vs Salary for training set")
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.show()
#
# # Plotting test set result into graphs
# plt.scatter(x_test, y_test, c='r')
# plt.plot(x_train, regression.predict(x_train), c='b')
# plt.title("Experience Vs Salary for test set")
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.show()
