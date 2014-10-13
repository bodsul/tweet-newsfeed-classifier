import simplejson
from tweetinfo import gettweetinfo
from gettweetmodule import gettweet
from cleantweet import TWIT

api = gettweetinfo()

#weather sources
weather_sources = ['weatherchannel', 'bbcweather',
                   'wunderground']

#get and clean weather tweets
a = []
for id in weather_sources:
    a+= gettweet(api, id, 50)

weather_tweets = TWIT(a)
weather_tweets.clean()


#write weather tweets to file as an array
f = open('weathertweets.txt', 'w')
simplejson.dump(weather_tweets.a, f)
f.close()
