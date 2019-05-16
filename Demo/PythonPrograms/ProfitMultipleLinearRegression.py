# Importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Importing dataSet
dataSet = pd.read_csv('../inputFiles/50_Startups.csv')
y_index = dataSet.columns.get_loc("Profit")

if y_index == (len(dataSet.columns)-1):
    x = dataSet.iloc[:, 0:y_index]

if y_index > 0 and y_index < (len(dataSet.columns)-1):
    x = dataSet.iloc[:, 0:y_index]
    x = x + dataSet.iloc[:, (y_index+1):len(dataSet)]

if y_index == 0:
    x = dataSet.iloc[:, -1:y_index:-1]

y = dataSet.iloc[:, y_index:(y_index+1)]

# Handling categorical values
states = pd.get_dummies(x['State'])
x = x.drop('State', axis=1)
x = pd.concat([x, states], axis=1)

# Checking for null values
if y['Profit'].isnull().sum() > 0:
    print("Taking care of null values of Profit column")
    y = y.fillna(y.mean())

columns = x.columns
for c in columns:
    if x[c].isnull().sum() > 0:
        print("Taking care of null values of {} column".format(c))
        x = x[c].fillna(x[c].mean())

# Splitting values into training and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# Fitting training set into model
regression = LinearRegression()
regression.fit(x_train, y_train)

# Predicting values
y_pred = regression.predict(x_test)
y_pred1 = regression.predict(x_train)

# calculating r2_score
diff = r2_score(y_test, y_pred)
print(diff)
diff1 = r2_score(y_train, y_pred1)
print(diff1)
