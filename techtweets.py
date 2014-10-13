import simplejson
from tweetinfo import gettweetinfo
from gettweetmodule import gettweet
from cleantweet import TWIT


api = gettweetinfo()

#list tech tweet sources
tech_sources = ['techreview', 'TechCrunch', 'techreview', 'ScienceTip', 'ScienceNews', 'sciam', 'ForbesTech', 'Techmeme', 'bbchealth',
                'NatGeo', 'WomensHealthMag', 'MensHealthMag',
                'guardianscience']

#get and clean tech tweets
a = []
for id in tech_sources:
    a+= gettweet(api, id, 10)
tech_tweets = TWIT(a)
tech_tweets.clean()

#write tech tweets to file as an array
f = open('techtweets.txt', 'w')
simplejson.dump(tech_tweets.a, f)
f.close()
