class GETTWEET:
    """class for getting and returning tweets from a bunch of users id's stored in different categories 
    in the dictionary object sources"""

    def __init__(self, api, sources):
        self.api = api
        self.sources = sources
        self.tweets ={}

    def return_tweets(self):
        
        for key in self.sources.keys():
            for id in self.sources[key]:
                "return last twenty tweets of user with twitter id"
                tweets = self.api.user_timeline(id, count = 15)
                for tweet in tweets:
                    "need encode to be able to store as a dict of arrays?"
                    if key in self.tweets.keys():
                        self.tweets[key].append(tweet.text.encode('utf-8'))
                    else:
                        a = []
                        a.append(tweet.text.encode('utf-8'))
                        self.tweets[key] = a

        return self.tweets
