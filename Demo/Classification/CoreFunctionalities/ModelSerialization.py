import pickle


class ModelSerialization:
    def saveModel(self, classifier, fileName):
        pkl_file = open(fileName, 'wb')
        pickle.dump(classifier, pkl_file)


