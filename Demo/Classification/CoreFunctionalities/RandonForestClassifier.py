from Demo.Classification.CoreFunctionalities.MLAlgorithmAbstract import MLAlgorithmAbstract
from sklearn.ensemble import RandomForestClassifier
import warnings
from sklearn.metrics import accuracy_score
from Demo.Classification.CoreFunctionalities.ModelSerialization import ModelSerialization
from Demo.Classification.ModelUsage.ModelDeserialization import ModelDeserialization


class ImplementAlgorithm(MLAlgorithmAbstract):
    def createAndUseModel(self, filePath, yColumn, xColumnNumerical=[], xColumnCategorical=[]):

        warnings.filterwarnings("ignore", category=FutureWarning)

        classifier = RandomForestClassifier(n_estimators=10)

        result = MLAlgorithmAbstract.handle_dataset(self, filePath, yColumn, xColumnNumerical, xColumnCategorical)
        classifier.fit(result[0][0], result[0][2].values.ravel())

        y_pred = classifier.predict(result[0][1])

        accuracy = accuracy_score(result[0][3], y_pred)

        print("Accuracy of training data", accuracy)

        if accuracy > 0.8:
            ModelSerialization.saveModel(self, classifier, '../inputFiles/RandomForestClassifier.pkl')
            ModelDeserialization.loadModel(self, '../inputFiles/RandomForestClassifier.pkl', yColumn, result[1])


implement = ImplementAlgorithm()
# implement.createAndUseModel('../inputFiles/Social_Network_Ads.csv', 'Purchased', ['Age', 'EstimatedSalary'], [])

implement.createAndUseModel('../inputFiles/schillingData.csv', 'Flag', [], ['Octamers'])