from flask import Flask, render_template

from twitter.api import get_subject_tweets


wergu = Flask(__name__)


@wergu.route('/')
def index():
    return render_template('index.html')


@wergu.route('/tweets/<subject>', strict_slashes=False)
def tweets(subject):
    return str(get_subject_tweets(subject))


@wergu.route('/procon')
def pro_con():
    issue_title = "#Trump2016"
    pro_list = [
        "Watching @realDonaldTrump on @jimmyfallon!!!!  Can't wait to say President Trump #Trump2016 #trumpnation @WeSupportTrump @trump2016fan",
        "Mr @realDonaldTrump just wanted you to know you have a huge following in Canada...They want you to win in #Trump2016 @DanScavino #TeamTrump",
        "@realDonaldTrump Genius #Trump2016 Just do it #MakeAmericaGreatAgain!!!! @realDonaldTrump @FallonTonight",
        "@realDonaldTrump you were amazing on @jimmyfallon @FallonTonight !! #Trump2016 very exciting!  Presidential & truly a joy to watch!"
    ]

    con_list = [
        "Every day, this waking nightmare of #donaldtrump ascending the polls truly makes me wonder if I'm in a twisted version of the Truman Show.",
        "DonaldTrump just another idiot silver spoon trust fund baby lk #GWBush avg Conservative 'Rich Guy Groupies' vote 4",
        "#DonaldTrump has ZERO military experience, but he's on record saying he knows more than many in the military or veterans? Just... wow.",
        "I can't believe that people are taking #donaldtrump seriously. He's the worst sort of idiot: one with an ego. He'll get us all killed."
    ]

    return render_template('procon.html', issue_title=issue_title, pro_list=pro_list, con_list=con_list)


def start():
    wergu.run(debug=True)
