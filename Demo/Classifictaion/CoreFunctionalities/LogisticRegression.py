from Demo.Classification.CoreFunctionalities.MLAlgorithmAbstract import MLAlgorithmAbstract
from sklearn.linear_model import LogisticRegression
import warnings
from sklearn.metrics import accuracy_score
from Demo.Classification.CoreFunctionalities.ModelSerialization import ModelSerialization


class ImplementAlgorithm(MLAlgorithmAbstract):
    def createAndUseModel(self, filePath, yColumn, xColumnNumerical=[], xColumnCategorical=[]):

        warnings.filterwarnings("ignore", category=FutureWarning)

        classifier = LogisticRegression()

        result = MLAlgorithmAbstract.handle_dataset(self, filePath, yColumn, xColumnNumerical, xColumnCategorical)
        classifier.fit(result[0], result[2].values.ravel())

        y_pred = classifier.predict(result[1])

        accuracy = accuracy_score(result[3], y_pred)

        if accuracy > 0.8:
            ModelSerialization.saveModel(self, classifier)


i = ImplementAlgorithm()
i.createAndUseModel('../inputFiles/Social_Network_Ads.csv', 'Purchased', ['Age', 'EstimatedSalary'], [])