from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import string

class TOKENIZE:
    def __init__(self, tweets):
        self.tweets = tweets
        self.tokenized_tweets = {}

    def tokenize(self):
        for key in self.tweets.keys():
            self.tokenized_tweets[key]= [word_tokenize(tweet) for tweet in self.tweets[key]]

    def remove_punctuation(self):
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        temp ={}
        for key in self.tokenized_tweets.keys():
            temp[key] = []
            for tweetwords in self.tokenized_tweets[key]:
                new_tweetwords=[]
                for word in tweetwords:
                    #take out punctuation using regex.sub
                    new_word = regex.sub('',word)
                    if not new_word == '':
                        new_tweetwords.append(new_word)
                temp[key].append(new_tweetwords)
        self.tokenized_tweets = temp

    def remove_stopwords(self):
        temp ={}
        for key in self.tokenized_tweets.keys():
            temp[key] =[]
            for tweetwords in self.tokenized_tweets[key]:
                new_tweetwords=[]
                for word in tweetwords:
                    #take out punctuation using regex.sub
                    if not word in stopwords.words('english'):
                        #convert to lower case
                        new_tweetwords.append(word.lower())
                temp[key].append(new_tweetwords)
        self.tokenized_tweets = temp

    def clean(self):
        self.tokenize()
        self.remove_punctuation()
        self.remove_stopwords()
        return self.tokenized_tweets
                        
            


