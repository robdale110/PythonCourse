"""
    Very simple web app
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Website content goes here!"

@app.route("/about/")
def about():
    return "This is the about page!"

if __name__ == '__main__':
    app.run(debug=True)
