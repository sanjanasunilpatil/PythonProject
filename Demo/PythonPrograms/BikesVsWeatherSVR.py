# Importing libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import r2_score
import pickle

# Importing dataset and split into 2 different csv files
dataSet = pd.read_csv('../inputFiles/bike_sharing.csv')

df_training = dataSet.sample(frac=0.8)
df_test = pd.concat([dataSet, df_training]).drop_duplicates(keep=False)

df_training.to_csv('../inputFiles/training_data.csv', header=True, index=None)
df_test.to_csv('../inputFiles/test_data.csv', header=True, index=None)

dataSet = pd.read_csv('../inputFiles/training_data.csv')
x1_index = dataSet.columns.get_loc("temp")
x2_index = dataSet.columns.get_loc("atemp")
x3_index = dataSet.columns.get_loc("hum")
x4_index = dataSet.columns.get_loc("windspeed")
y_index = dataSet.columns.get_loc("cnt")

x = dataSet.iloc[:, [x1_index, x2_index, x3_index, x4_index]]
y = dataSet.iloc[:, y_index:(y_index+1)]

# Checking for null values
if y['cnt'].isnull().sum() > 0:
    print("Taking care of null values of cnt column")
    y = y.fillna(y.mean())

for c in x.columns:
    if x[c].isnull().sum() > 0:
        print("Taking care of null values of temp column")
        x[c] = x[c].fillna(x.mean())

# Feature scaling
sc_x = StandardScaler()
x = sc_x.fit_transform(x)

# Splitting dataset into training and test dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Fitting model
regression = SVR(kernel='rbf', gamma='auto')
regression.fit(x_train, y_train.values.ravel())

# Predicting values of test data
y_pred = regression.predict(x_test)

# Calculating accuracy of trained model
accuracy = r2_score(y_test, y_pred)
print("Accuracy of model ", accuracy)

# Saving model into pickle file
if accuracy > 0.8:
    file_name = '../inputFiles/randomForestRegression.pkl'
    pkl_file = open(file_name, 'wb')
    model = pickle.dump(regression, pkl_file)
    pkl_file.close()

# Load pkl model to predict data
    pkl_file = open(file_name, 'rb')
    model = pickle.load(pkl_file)

# Read data, Predict y values and calculate accuracy
    dataSet_testdata = pd.read_csv('../inputFiles/test_data.csv')
    x_testdata = dataSet_testdata.iloc[:, [x1_index, x2_index, x3_index, x4_index]]
    y_testdata = dataSet_testdata.iloc[:, y_index:(y_index+1)]

    y_pred = model.predict(x_testdata)
    accuracy_pkl = r2_score(y_testdata, y_pred)

    print("Accuracy by pickle model ", accuracy_pkl)
