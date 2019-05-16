# Importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import pickle

# Importing dataset and splitting dataset into 2 different csv files
dataSet = pd.read_csv('../inputFiles/Position_Salaries.csv')

df_training = dataSet.sample(frac=0.7)
df_test = pd.concat([dataSet, df_training]).drop_duplicates(keep=False)

df_training.to_csv('../inputFiles/training_data.csv', header=True, index=None)
df_test.to_csv('../inputFiles/test_data.csv', header=True, index=None)

dataSet = pd.read_csv('../inputFiles/training_data.csv')
x_index = dataSet.columns.get_loc("Level")
y_index = dataSet.columns.get_loc("Salary")

x = dataSet.iloc[:, x_index:(x_index+1)]
y = dataSet.iloc[:, y_index:(y_index+1)]


# Checking for null values
if y['Salary'].isnull().sum() > 0:
    print("Taking care of null values of Salary column")
    y = y.fillna(y.mean())

if x['Level'].isnull().sum() > 0:
    print("Taking care of null values of Level column")
    x = x.fillna(x.mean())

# Feature scaling
scX = StandardScaler()
x = scX.fit_transform(x)

# Splitting data into training and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# Fitting training data into model
regression = DecisionTreeRegressor()
regression.fit(x_train, y_train)

# Using model to predict test data
y_pred = regression.predict(x_test)

# Calculating accuracy
accuracy = r2_score(y_test, y_pred)
print("Accuracy from model is : ", accuracy)

# # Dumping model into pickle
# file_name = '../inputFiles/DecisionTreeRegression.pkl'
# pkl_file = open(file_name, 'wb')
# model = pickle.dump(regression, pkl_file)
#
# # Loading pickle model to predict data from test_data.csv file
# pkl_file = open(file_name, 'rb')
# model_pkl = pickle.load(pkl_file)
#
# dataSet_testdata = pd.read_csv('../inputFiles/test_data.csv')
#
# x_testdata = dataSet_testdata.iloc[:, x_index:(x_index+1)]
# y_testdata = dataSet_testdata.iloc[:, y_index:(y_index+1)]
#
# y_pred_pkl = model_pkl.predict(x_testdata)
#
# # Calculating accuracy from pickle model
# accuracy_pk = r2_score(y_testdata, y_pred_pkl)
# print("Accuracy by pickle model ", accuracy_pk)
