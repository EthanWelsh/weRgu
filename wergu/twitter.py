import tweepy

from secrets import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def get_subject_tweets(subject):
    tweet_list = []
    results = api.search(subject)
    for tweet in results:
        tweet_list.append(tweet.text)
    return str(tweet_list)
