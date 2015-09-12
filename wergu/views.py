from flask import Flask, render_template


wergu = Flask(__name__)

@wergu.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    wergu.run(debug=True)
