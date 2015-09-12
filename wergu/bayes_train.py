from nltk.classify import NaiveBayesClassifier as NBC


def word_features(words):
    return dict([(word, True) for word in words])


def train_sad(positive_file, negative_file):
    """
    :param positive_file: this file will contain all the positive sentiment tweets
    :param negative_file: this file will contain all the negative sentiment tweets
    :return: bayesian_classifier of class NaiveBayesClassifier clf
    """

    with open(positive_file, 'r') as pos_tweets:
        pos_tweets_list = [(line, 'pos') for line in pos_tweets.readlines()]

    with open(negative_file, 'r') as neg_tweets:
        neg_tweets_list = [(line, 'neg') for line in neg_tweets.readlines()]

    pos_cutoff = int(len(pos_tweets_list) * 0.9)
    neg_cutoff = int(len(neg_tweets_list) * 0.9)

    return NBC.train(pos_tweets_list[:pos_cutoff] + neg_tweets_list[:neg_cutoff])


def main():
    clf = train_sad('data/pos_tweets.txt', 'data/neg_tweets.txt')
    clf.show_most_informative_features()

    # clf.classify(tweet_we_want_to_classify)


if __name__ == 'main':
    main()
