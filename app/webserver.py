from flask import Flask, render_template

from twitter.api import get_subject_tweets
import bayesian_analysis.sentiment

wergu = Flask(__name__)
nbc = None


@wergu.route('/')
def index():
    return render_template('index.html')


@wergu.route('/tweets/<subject>', strict_slashes=False)
def tweets(subject):
    return str(get_subject_tweets(subject))


@wergu.route('/procon/<subject>')
def pro_con(subject):
    issue_title = subject

    list_of_tweets = get_subject_tweets(subject)
    con_tweets = []
    pro_tweets = []

    for tweet in list_of_tweets:
        sentiment_value = bayesian_analysis.sentiment.get_tweet_sentiment(tweet)
        if sentiment_value < -.3:
            con_tweets.append(tweet)
        elif sentiment_value > .3:
            pro_tweets.append(tweet)

    return render_template('procon.html', issue_title=issue_title, pro_list=pro_tweets, con_list=con_tweets)

def start(naive_bayes_classifier):
    global nbc

    wergu.run()
    nbc = naive_bayes_classifier
