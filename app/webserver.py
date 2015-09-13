from flask import Flask, render_template

from twitter.api import get_subject_tweets
import bayesian_analysis.sentiment as sen

import re

wergu = Flask(__name__)
nbc = None


@wergu.route('/')
def index():
    return render_template('index.html')

@wergu.route('/about')
def about():
    print("I HERE")
    return render_template('about.html')

@wergu.route('/tweets/<subject>', strict_slashes=False)
def tweets(subject):
    return str(get_subject_tweets(subject))


@wergu.route('/procon/<subject>')
def pro_con(subject):
    global nbc

    tweets = get_subject_tweets(subject)

    tweets = map(lambda x: re.sub(r'([^\s\w]|_)+', '', x.lower()), tweets)

    print tweets

    pro = filter(lambda x: sen.get_tweet_sentiment(x, nbc) > 0.5, tweets)
    neg = filter(lambda x: sen.get_tweet_sentiment(x, nbc) <= 0.5, tweets)

    print pro

    return render_template('procon.html', issue_title=subject, pro_list=pro, con_list=neg)

def start(naive_bayes_classifier):
    global nbc

    wergu.run()
    nbc = naive_bayes_classifier
