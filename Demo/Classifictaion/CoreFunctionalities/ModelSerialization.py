import pickle


class ModelSerialization:
    def saveModel(self, classifier):
        file_name = '../inputFiles/LogisticRegression.pkl'
        pkl_file = open(file_name, 'wb')
        pickle.dump(classifier, pkl_file)


