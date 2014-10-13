import simplejson
from tweetinfo import gettweetinfo
from gettweetmodule import gettweet
from cleantweet import TWIT


api = gettweetinfo()

#list sports sources
sports_sources = ['espn', 'BBC Sport', 'Soccernet', 'GolfChannel','HBOboxing', 'GolfChannel', 'NHL', 'NFL', 'MLB', 'Olympics', 'NBA']

#get and clean sports tweets
a = []
for id in sports_sources:
    a+= gettweet(api, id, 15)

sports_tweets = TWIT(a)
sports_tweets.clean()

#write sports tweets to file as an array
f = open('sportstweets.txt', 'w')
simplejson.dump(sports_tweets.a, f)
f.close()
