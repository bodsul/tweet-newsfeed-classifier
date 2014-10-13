import simplejson
from tweetinfo import gettweetinfo
from gettweetmodule import gettweet
from cleantweet import TWIT


api = gettweetinfo()

#list financial, business and economic sources
fin_sources = ['FinancialTimes', 'RiskMagazine', 'StockTwits', 'Vanguard_Group', 'dealbook','hedge_funds', 'BloombergNews' ]

#get and financial tweets
a = []
for id in fin_sources:
    a+= gettweet(api, id, 20)
fin_tweets = TWIT(a)
fin_tweets.clean()

#write financial tweets to file as an array
f = open('fintweets.txt', 'w')
simplejson.dump(fin_tweets.a, f)
f.close()
