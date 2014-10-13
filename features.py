#returns dictionary containing features of tweets given relevant words
def get_features(tweet, rel_words):
    tweet_words = tweet.split()
    features = {}
    for word in rel_words:
        features['has(%s)' % word] = (word in tweet_words)
    return features
    