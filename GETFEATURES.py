import random

def get_features(tokenized_tweet, topwords):
    #tweet_words = tokenized_tweet
    features = {}
    topwordsarray=[]
    for key in topwords.keys():
        topwordsarray+= topwords[key]
    
    for word in topwordsarray:
        features['has(%s)' % word] = (word in tokenized_tweet)
    return features

class GETFEATURES:
    def __init__(self, tokenized_tweets, topwords):
        self.tokenized_tweets = tokenized_tweets
        self.topwords = topwords
        self.data = []

    def getdata(self):
        data = []
        for key in self.tokenized_tweets.keys():
            data += [(tokenized_tweet, key) for tokenized_tweet in self.tokenized_tweets[key]]
        random.shuffle(data)
        return data

    def getfeatures(self):
        #should be more efficient here and unpack  self.topwords to an array
        data = self.getdata()
        self.data = [(get_features(tokenized_tweet, self.topwords), label) for (tokenized_tweet,label) in data]
        return self.data



        