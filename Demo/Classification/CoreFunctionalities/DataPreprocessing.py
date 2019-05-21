# Importing libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


class DataPreprocessingBase:

    # Importing dataset, split into 2 different csv files and create train and test data set
    def handle_dataset(self, filePath, yColumn, xColumnNumerical=[], xColumnCategorical=[]):
        dataSet = pd.read_csv(filePath)

        if len(xColumnCategorical) > 0:
            length_old = len(dataSet.columns)
            dataSet = self.handleCategoricalData(dataSet, xColumnCategorical)
            length_new = len(dataSet.columns)

        df_training = dataSet.sample(frac=0.8)
        df_test = pd.concat([dataSet, df_training]).drop_duplicates(keep=False)

        df_training.to_csv('../inputFiles/training_data.csv', header=True, index=None)
        df_test.to_csv('../inputFiles/test_data.csv', header=True, index=None)

        dataSet = pd.read_csv('../inputFiles/training_data.csv')

        y_index = dataSet.columns.get_loc(yColumn)
        y = dataSet.iloc[:, y_index:(y_index + 1)]
        x = pd.DataFrame()
        x_index = []

        if len(xColumnNumerical) > 0:
            for i in xColumnNumerical:
                x_index.append(dataSet.columns.get_loc(i))
            x = dataSet.iloc[:, x_index]

        if len(xColumnCategorical) > 0:
            if len(xColumnNumerical) > 0:
                x = pd.concat([x, dataSet.iloc[:, (length_old-1):length_new]], axis=1)
            else:
                x = dataSet.iloc[:, (length_old-1):length_new]

            # For getting x indices into single place
            for i in range((length_old-1), length_new, 1):
                x_index.append(i)

        for i in xColumnNumerical:
            if x[i].isnull().sum() > 0:
                self.nullHandling(x[i])

        x = self.featureScaling(x)

        result = self.splitData(x, y)

        return result, x_index

    # Handling categorical data
    def handleCategoricalData(self, dataSet=pd.DataFrame(), xColumnCategorical=[]):

        for i in xColumnCategorical:
            new_columns = pd.get_dummies(dataSet[i])
            dataSet = dataSet.drop(i, axis=1)
            dataSet = pd.concat([dataSet, new_columns], axis=1)
        return dataSet

    # Feature scaling
    def featureScaling(self, x):
        scX = StandardScaler()
        x = scX.fit_transform(x)
        return x

    # Handling Null data
    def nullHandling(self, x):
        x = x.fillna(x.mean())

    # Splitting dataset into training and test dataset
    def splitData(self, x=pd.DataFrame(), y=pd.DataFrame()):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        return x_train, x_test, y_train, y_test

#
# d = DataPreprocessingBase()
#
# d.handle_dataset('../inputFiles/Position_Salaries.csv', 'Salary', [], ['Position'])
