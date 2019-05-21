from Demo.Classification.CoreFunctionalities.DataPreprocessing import DataPreprocessingBase


class MLAlgorithmAbstract(DataPreprocessingBase):

    # abstract method
    def createAndUseModel(self, filePath, yColumn, xColumnNumerical=[], xColumnCategorical=[]):
        pass











