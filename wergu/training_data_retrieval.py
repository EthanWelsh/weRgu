import re
import zipfile

import urllib
import os


def get_sad_tweets_file():
    url = 'http://thinknook.com/wp-content/uploads/2012/09/Sentiment-Analysis-Dataset.zip'

    urllib.urlretrieve (url, 'data/Sentiment-Analysis-Dataset.zip')

    with open('data/Sentiment-Analysis-Dataset.zip', 'rb') as fh:
        z = zipfile.ZipFile(fh)
        for name in z.namelist():
            z.extract(name, 'data')


def get_classified_tweet_files():

    # If we don't already have the Sentiment Analysis Dataset.csv file, download it.
    if not os.path.isfile('data/Sentiment Analysis Dataset.csv'):
        get_sad_tweets_file()

    tweets = []

    with open("data/Sentiment Analysis Dataset.csv", "r") as f:
        next(f)
        for line in f:
            tweets.append(line.strip().split(','))

    sentiment_labeled = map(lambda x: (int(x[1]), re.sub(r'([^\s\w]|_)+', '', x[3].lower()).strip()), tweets)

    pos_tweets = map(lambda y: y[1], filter(lambda x: x[0] == 1, sentiment_labeled))
    neg_tweets = map(lambda y: y[1], filter(lambda x: x[0] == 0, sentiment_labeled))

    with open('data/pos_tweets.txt', 'w') as out:
        out.write('\n'.join(pos_tweets))

    with open('data/neg_tweets.txt', 'w') as out:
        out.write('\n'.join(neg_tweets))
