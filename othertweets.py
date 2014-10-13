import simplejson
from tweetinfo import gettweetinfo
from gettweetmodule import gettweet
from cleantweet import TWIT

api = gettweetinfo()

#random/other sources
other_sources = ['Seldomaniac', 'Callamasta', 'jwharris', 'don_brown']

#get and clean other/random tweets
a = []
for id in other_sources:
    a+= gettweet(api, id, 30)

other_tweets = TWIT(a)
other_tweets.clean()


#write other/random tweets to file as an array
f = open('othertweets.txt', 'w')
simplejson.dump(other_tweets.a, f)
f.close()
