import nltk
class CLASSIFIER:
    def __init__(self, data):
        self.data = data

    def classify(self):
        #define training set and test set
        train_data, test_data = self.data[800:], self.data[:200]
        learner = nltk.NaiveBayesClassifier.train(train_data)
        accuracy= nltk.classify.accuracy(learner, test_data)
        return accuracy
            
