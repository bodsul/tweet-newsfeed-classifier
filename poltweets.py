import simplejson
from tweetinfo import gettweetinfo
from gettweetmodule import gettweet
from cleantweet import TWIT


api = gettweetinfo()

#list political sources
pol_sources = ['_politicalworld', 'BBCPolitics', 'PoliticalTicker', 'ForeignPolicy']

#get and clean political tweets
a = []
for id in pol_sources:
    a+= gettweet(api, id, 40)

pol_tweets = TWIT(a)
pol_tweets.clean()

#write political tweets to file as an array
f = open('poltweets.txt', 'w')
simplejson.dump(pol_tweets.a, f)
f.close()
