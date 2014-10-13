import simplejson
from tweetinfo import gettweetinfo
from gettweetmodule import gettweet
from cleantweet import TWIT

api = gettweetinfo()

#list entertainment sources
ent_sources = ['MTV', 'Rock Music', 'TheGRAMMYs', 'TheAcademy', 'bbcentertain',  'EntMagazine']

#get and clean entertainment tweets
a = []
for id in ent_sources:
    a+= gettweet(api, id, 20)

ent_tweets = TWIT(a)
ent_tweets.clean()

#write entertainment tweets to file as an array
f = open('enttweets.txt', 'w')
simplejson.dump(ent_tweets.a, f)
f.close()