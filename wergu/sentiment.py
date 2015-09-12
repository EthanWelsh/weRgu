def get_sentence_sentiment(sentence):
    """Given a string, will split that string into several words, analyze them using naive base, and then output the
    probability from -1.0 to 1.0 that the string in question in negative/positive in mood and nature.

    :param sentence: The sentence that you will be measuring.
    :return: sentiment: The sentiment grade that shows how positive or negative a sentence is.
    :return: probability: The level of precision behind the bayesian forecast
    """

    words = sentence.split(' ')
    sentiments = [get_word_sentiment(word) for word in words]
    return sum(sentiments[0]) / float(len(words)), sum(sentiments[1]) / float(len(words))


def get_word_sentiment(word):
    """Given a single word, will analyze said word using naive base, and then output the
    probability from -1.0 to 1.0 that the word in question in negative/positive in mood and nature.

    :param word: The word that you will be measuring.
    :return: sentiment: The sentiment grade that shows how positive or negative a word is.
    :return: probability: The level of precision behind the bayesian forecast
    """
    pass

