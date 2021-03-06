import os

from bayesian_analysis.training_data_retrieval import get_classified_tweet_files
from bayesian_analysis.bayes_train import train_sad, write_nbc_as_pickle, get_nbc_from_pickle
import app.webserver
import app.webserver as ws

nbc = None


def main():
    global nbc

    print("Getting NBC...")
    nbc = get_nbc()
    print("Got NBC!")
    print("Starting web server...")
    ws.nbc = nbc
    app.webserver.start()


def get_nbc():
    global nbc

    if nbc is not None:
        return nbc

    if not os.path.isfile('data/model.pkl'):
        print("No pickle found... Searching for training files...")

        if not os.path.isfile('data/pos_tweets.txt') or not os.path.isfile('data/neg_tweets.txt'):
            print("Training files not found... Downloading file and separating tweets...")
            get_classified_tweet_files()

        print("Training NBC...")
        nbc = train_sad(positive_file='data/pos_tweets.txt', negative_file='data/neg_tweets.txt')

        print("Saving NBC as pickle for later...")
        write_nbc_as_pickle(nbc)
        print("Saved...")
    else:
        print('Reading in NBC from pickle...')
        nbc = get_nbc_from_pickle('data/model.pkl')

    return nbc


if __name__ == '__main__':
    if nbc is None:
        main()
