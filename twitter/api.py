import tweepy

from app.auth.secrets import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def get_subject_tweets(subject):
    tweet_list = []
    try:
        for tweet in tweepy.Cursor(api.search, q=subject, count=15, lang="en").items(15):
            split_tweet = tweet.text.split()
            split_tweet = filter(lambda x: 'http' not in x, split_tweet)
            tweet_list.append(' '.join(split_tweet))
    except Exception as e:
        print e

    return tweet_list
