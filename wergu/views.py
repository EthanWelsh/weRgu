from flask import Flask, render_template

wergu = Flask(__name__)

@wergu.route('/')
def index():
    return "Hi!"

if __name__ == "__main__":
    wergu.run(debug=True)
