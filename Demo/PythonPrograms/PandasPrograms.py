import numpy as np
import pandas as pd


class Demo:
    def seriesBasics(self):
        a = np.array([1, 2, 3.0, 4])
        s = pd.Series(a, ['1st Row', '2nd Row', '3rd Row', '4th Row'], dtype=int)
        print("Series: ", s)

        l1 = list(s)
        print("List created by converting series into list is {} and its type is {}".format(l1, type(l1)))

    def arithmaticOperations(self):
        s1 = pd.Series([2, 4, 6, 8, 10])
        s2 = pd.Series([1, 3, 5, 7, 9])

        print("Addition: \n", s1 + s2)
        print("Addition of all elements of both series: \n", s1.sum() + s2.sum())
        print("Subtraction: \n", s1 - s2)
        print("Multiplication: \n", s1 * s2)
        print("Division: \n", s1 / s2)

    def raisedPower(self):
        a = np.array([0, 1, 2, 3, 4, 5, 6])
        a1 = np.array([0, 1, 8, 27, 64, 125, 216])

        print("Raised to powers from second array ", np.power(a, a1))
        print("Raised by 3 ", np.power(a, 3))

    def dataFrameBasics(self):
        exam_data = {
            'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
                     'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

        df = pd.DataFrame(exam_data, index=labels)
        print("Original Data Frame: \n", df)
        print("\nInformation about given data frame: \n", df.info())
        print("\nFirst 3 rows: \n", df.head(3))
        print("\nFirst column : \n", df['name'])
        print("\n2nd column : \n", df['score'])

        print("\nPrinting 4 rows of first 2 columns : \n", df.iloc[[1, 3, 5, 6], [1, 2]])

    def attemptsGreaterThan2(self):
        exam_data = {
            'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
                     'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

        df = pd.DataFrame(exam_data, index=labels)

        l1 = []
        for i, j in df.iterrows():         # This for loop travers through row and i will store index value
            if df.loc[i]['attempts'] > 2:  # This will fetch exact value of attempt for particular row and will get compared to 2
                l1.append(i)               # Here index will get added into list and that list will be passed to loc() function

        print("Records greater than 2 attempts \n", df.loc[l1])

    def noOfRowsColumns(self):
        exam_data = {
            'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
                     'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

        df = pd.DataFrame(exam_data, index=labels)
        count_rows = 0
        count_columns = 0

        for i in df.iteritems():    # Iterates over columns
            count_columns = count_columns + 1

        for i in df.iterrows():     # Iterates over rows
            count_rows = count_rows + 1

        print("Total number of columns are: ", count_columns)
        print("Total number of rows are: ", count_rows)

d = Demo()
# d.seriesBasics()
# d.arithmaticOperations()
# d.raisedPower()
# d.dataFrameBasics()
# d.attemptsGreaterThan2()
d.noOfRowsColumns()