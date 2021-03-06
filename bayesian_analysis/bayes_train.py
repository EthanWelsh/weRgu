import cPickle as pickle

from nltk.classify import NaiveBayesClassifier as NBC


def word_features(words):
    return dict([(word, True) for word in words])


def train_sad(positive_file, negative_file):
    """
    :param positive_file: this file will contain all the positive sentiment tweets
    :param negative_file: this file will contain all the negative sentiment tweets
    :return: bayesian_classifier of class NaiveBayesClassifier clf
    """

    pos_tweets_list = []
    neg_tweets_list = []

    with open(positive_file, 'r') as pos_tweets:
        for line in pos_tweets.readlines():
            word_dict = {word: True for word in line.split()}
            pos_tweets_list.append((word_dict, 'pos'))

    with open(negative_file, 'r') as neg_tweets:
        for line in neg_tweets.readlines():
            word_dict = {word: True for word in line.split()}
            neg_tweets_list.append((word_dict, 'neg'))

    pos_cutoff = int(len(pos_tweets_list) * 0.9)
    neg_cutoff = int(len(neg_tweets_list) * 0.9)

    return NBC.train(pos_tweets_list[:pos_cutoff] + neg_tweets_list[:neg_cutoff])


def write_nbc_as_pickle(nbc, file_name='data/model.pkl'):
    pickle.dump(nbc, open(file_name, 'wb'), -1)


def get_nbc_from_pickle(file_name='data/model.pkl'):
    return pickle.load(open(file_name, 'rb'))


def get_sad():
    return train_sad('data/pos_tweets.txt', 'data/neg_tweets.txt')


def main():
    clf = get_sad()
    clf.show_most_informative_features()


if __name__ == '__main__':
    main()
