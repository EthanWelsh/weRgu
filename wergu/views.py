from flask import Flask, render_template

from twitter import get_subject_tweets

wergu = Flask(__name__)


@wergu.route('/')
def index():
    return render_template('index.html')

@wergu.route('/tweets/<subject>', strict_slashes=False)
def tweets(subject):
    return get_subject_tweets(subject)

if __name__ == "__main__":
    wergu.run(debug=True)
