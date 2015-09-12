def get_subject(subject, nbc):
    """
    :param subject: The subject/issue that you are interested in seeing
    :return: positive: a list of tweets that embody a positive sentiment towards the given subject area.
    :return: negative: a list of tweets that embody a negative sentiment towards the given subject area.
    """

def get_tweet_sentiment(sentence, nbc):
    """Given a string, will split that string into several words, analyze them using naive base, and then output the
    probability from -1.0 to 1.0 that the string in question in negative/positive in mood and nature.

    :param sentence: The sentence that you will be measuring.
    :return: sentiment: The sentiment grade that shows how positive or negative a sentence is.
    """

    words = sentence.split(' ')
    sentiments = [get_word_sentiment(word, nbc) for word in words]
    return sum(sentiments) / float(len(words))


def get_word_sentiment(word, nbc):
    """Given a single word, will analyze said word using naive base, and then output the
    probability from -1.0 to 1.0 that the word in question in negative/positive in mood and nature.

    :param word: The word that you will be measuring.
    :return: sentiment: The sentiment grade that shows how positive or negative a word is.
    """

    return nbc.classify({word:True})
