#returns recent n tweets of a user
def gettweet(api, id, n):
    a = []
    tweets = api.user_timeline(id, count = n)
    for tweet in tweets:
        a.append(tweet.text.encode('utf-8'))

    return a


