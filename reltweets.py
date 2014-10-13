import simplejson
from tweetinfo import gettweetinfo
from gettweetmodule import gettweet
from cleantweet import TWIT

api = gettweetinfo()

#list religious sources
rel_sources = ['news_va_en', 'Buddhism_Now', 'HinduismToday', 'Pearlsofprophet', 'YourJudaism']

#get and clean religious tweets
a = []
for id in rel_sources:
    a+= gettweet(api, id, 25)

rel_tweets = TWIT(a)
rel_tweets.clean()

#write religious tweets to file as an array
f = open('reltweets.txt', 'w')
simplejson.dump(rel_tweets.a, f)
f.close()
