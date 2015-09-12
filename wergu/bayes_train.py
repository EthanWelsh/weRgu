import nltk.classify.util
from nltk.classify import NaiveBayesClassifier as NBC
from nltk.corpus import movie_reviews

def word_features(words):
    return dict( [(word, True) for word in words] )

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

tweet = "Watching @realDonaldTrump on @jimmyfallon!!!! Can't wait to say President Trump #Trump2016 #trumpnation @WeSupportTrump @Trump2016Fan"

neg_features = [ (word_features(movie_reviews.words(fileids=[f])), 'neg') for f in negids ]
pos_features = [ (word_features(movie_reviews.words(fileids=[f])), 'pos') for f in posids ]

twe = word_features(tweet.split(' '))

neg_cutoff = int(len(neg_features) * 0.9)
pos_cutoff = int(len(pos_features) * 0.9)

train_features = neg_features[:neg_cutoff] + pos_features[:pos_cutoff]
test_features = neg_features[neg_cutoff:] + pos_features[pos_cutoff:]

print "Training!"

clf = NBC.train(train_features)
print "Accuracy {0}".format( nltk.classify.util.accuracy(clf, test_features))
clf.show_most_informative_features()
print clf.classify(twe)
