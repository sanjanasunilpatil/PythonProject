import pickle
import pandas as pd
from sklearn.metrics import accuracy_score


class ModelDeserialization:
    # Load model from pickle and use same to predict test values
    def loadModel(self, file_name, yColumn, x_index=[]):
        pkl_file = open(file_name, 'rb')
        pkl_model = pickle.load(pkl_file)

        dataset = pd.read_csv('../inputFiles/test_data.csv')

        y_index = dataset.columns.get_loc(yColumn)
        y_test = dataset.iloc[:, y_index:(y_index + 1)]
        x_test = dataset.iloc[:, x_index]

        y_pred = pkl_model.predict(x_test)

        accuracy_pkl = accuracy_score(y_test, y_pred)

        print("Accuracy by pickle model ", accuracy_pkl)
