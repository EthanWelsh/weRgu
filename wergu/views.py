from flask import Flask, render_template

from secrets import consumer_key, consumer_secret, access_token, access_token_secret

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

wergu = Flask(__name__)


@wergu.route('/')
def index():
    return render_template('index.html')

@wergu.route('/tweets', strict_slashes=False)
def tweets():
    tweet_list = []
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        tweet_list.append(tweet.text)
    return str(tweet_list)

if __name__ == "__main__":
    wergu.run(debug=True)
