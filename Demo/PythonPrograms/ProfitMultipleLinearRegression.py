# Importing libraries
import pandas as pd

# Importing dataSet
dataSet = pd.read_csv('../inputFiles/50_Startups.csv')
y_index = dataSet.columns.get_loc("Profit")
x = pd.DataFrame()

if y_index == (len(dataSet.columns)-1):
    x = x.update(dataSet.iloc[:, 0:y_index])
if y_index > 0 and y_index < len(dataSet.columns):
    x = dataSet.iloc[:, 0:y_index]
    x = x + dataSet.iloc[:, (y_index+1):len(dataSet)]
if y_index == 0:
    x = dataSet.iloc[:, -1:y_index:-1]

y = dataSet.iloc[:, y_index:(y_index+1)]
print(x)
# Checking for categorical values

