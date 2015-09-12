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

    return render_template('procon.html', issue_title="", pro_list=[], con_list=[])

def start(naive_bayes_classifier):
    global nbc

    wergu.run()
    nbc = naive_bayes_classifier
