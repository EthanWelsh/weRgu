import re
import zipfile

import wget

url = 'http://thinknook.com/wp-content/uploads/2012/09/Sentiment-Analysis-Dataset.zip'
wget.download(url)

with open('Sentiment-Analysis-Dataset.zip', 'rb') as fh:
    z = zipfile.ZipFile(fh)
    for name in z.namelist():
        z.extract(name, '.')

tweets = []

with open("Sentiment Analysis Dataset.csv", "r") as f:
    next(f)
    for line in f:
        tweets.append(line.strip().split(','))

sentiment_labeled = map(lambda x: (int(x[1]), re.sub(r'([^\s\w]|_)+', '', x[3].lower()).strip()), tweets)

pos_tweets = map(lambda y: y[1], filter(lambda x: x[0] == 1, sentiment_labeled))
neg_tweets = map(lambda y: y[1], filter(lambda x: x[0] == 0, sentiment_labeled))

with open('pos_tweets.txt', 'w') as out:
    out.write('\n'.join(pos_tweets))

with open('neg_tweets.txt', 'w') as out:
    out.write('\n'.join(neg_tweets))

print len(pos_tweets)
print len(neg_tweets)
