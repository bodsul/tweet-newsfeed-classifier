from topwords import gettop
from features import get_features
from converttweettoarray import *
import nltk
import random

#list labels
labels = {1: 'science, tech and health', 2:'business, economy and finance', 3: 'politics', 4: 'sports', 5:'religion/religious teachings', 6: 'entertainment', 7: 'jobs and careers', 8:'weather', 9:'other'}

#other = 'event or news', 'fact or information sharing', 'personal'

#get most relevant words from tweets
rel_words = gettop('techtweets.txt')
rel_words+= gettop('fintweets.txt')
rel_words+= gettop('poltweets.txt')
rel_words+= gettop('sportstweets.txt')
rel_words+= gettop('reltweets.txt')
rel_words+= gettop('enttweets.txt')
rel_words+= gettop('jctweets.txt')
rel_words+= gettop('weathertweets.txt')
rel_words+= gettop('othertweets.txt')

#random shuffle relevant words
#random.shuffle(rel_words)

#create labelled dataset

data = [(tweet, '1') for tweet in copy_to_array('techtweets.txt')]

data+= [(tweet, '2') for tweet in copy_to_array('fintweets.txt')]

data+=[(tweet, '3') for tweet in copy_to_array('poltweets.txt')]
        
data+=[(tweet, '4') for tweet in copy_to_array('sportstweets.txt')]

data+=[(tweet, '5') for tweet in copy_to_array('reltweets.txt')]
        
data+=[(tweet, '6') for tweet in copy_to_array('enttweets.txt')]
    
data+= [(tweet, '7') for tweet in copy_to_array('jctweets.txt')]
        
data+= [(tweet, '8') for tweet in copy_to_array('weathertweets.txt')]
    
data+=[(tweet, '9') for tweet in copy_to_array('othertweets.txt')] 
        
random.shuffle(data)
        
#create labelled data set with features extracted
data_features = [(get_features(tweet, rel_words), label) for (tweet,label) in data]
        
#define training set and test set
train_data, test_data = data_features[400:], data_features[:200]
        
        
classifier = nltk.NaiveBayesClassifier.train(train_data)
        
print nltk.classify.accuracy(classifier, test_data)

#print rel_words[450:499]
#print copy_to_array('weathertweets.txt')
#print test_data
        

        
