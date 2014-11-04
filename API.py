from GETTWEET import*
from CLEANTWEETS import*
from TOKENIZE import*
from TOP import TOP
from GETFEATURES import*
from CLASSIFIER import*
import sys
import simplejson

#insert path containing a file called tweetinfo.py with private  twitter developer information
sys.path.insert(0,"../private_src")
from tweetinfo import gettweetinfo

class API:
    'class..'
    def __init__(self, sources):
        
        self.api = gettweetinfo()#this may need to be edited to method which returns user's private twitter api
        self.sources = sources
        self.tweets ={}
        self.tokenized_tweets={}
        self.topwords ={}
        self.data=[]
        
    def gettweets(self):
        gettweet = GETTWEET(self.api, self.sources)
        self.tweets = gettweet.return_tweets()
    
    def cleantweets(self):
        cleantweet = CLEANTWEETS(self.tweets)
        self.tweets = cleantweet.clean()
    
    def tokenizetweets(self):
        tokenizer = TOKENIZE(self.tweets)
        self.tokenized_tweets = tokenizer.clean()
    
    def writetofile(self):
        for key in self.sources.keys():
            f = open('%s.txt' % key, 'w')
            simplejson.dump(self.tokenized_tweets[key], f)
            f.close()
            
    def gettop(self):
        top = TOP(self.tokenized_tweets)
        self.topwords = top.gettopwords()
        return self.topwords

    def getfeatures(self):
        feature_gen = GETFEATURES(self.tokenized_tweets, self.topwords)
        self.data = feature_gen.getfeatures()

    def train(self):
        classifier = CLASSIFIER(self.data)
        return classifier.classify()
        
        
        
        
        

    
            
        
