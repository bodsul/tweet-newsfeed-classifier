import simplejson
from tweetinfo import gettweetinfo
from gettweetmodule import gettweet
from cleantweet import TWIT

api = gettweetinfo()

#job and careers sources
jc_sources = ['GuardianCareers', 'CareerBuilder', 'LinkedIn']

#get and clean job and careers tweets
a = []
for id in jc_sources:
    a+= gettweet(api, id, 50)

jc_tweets = TWIT(a)
jc_tweets.clean()

#write job and career tweets to file as an array
f = open('jctweets.txt', 'w')
simplejson.dump(jc_tweets.a, f)
f.close()
