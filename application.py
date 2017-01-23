from flask import Flask, redirect, render_template, request, url_for

import helpers
import nltk
import sys
import os
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index.html"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)
    
    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    
    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)

    # TODO
    # probably would be better for me to put this in its own .py file and call it that way rather than making this
    # code more complex
    tokenizer = nltk.tokenize.TweetTokenizer()
    
    sub_score = 0
    tweet_score = []
    positive = 0
    negative = 0
    neutral = 0
    
    for tweet in tweets:
        tokens = tokenizer.tokenize(tweet)
        # print(tokens)
        for token in tokens:
            sub_score = sub_score + analyzer.analyze(token)
        tweet_score.append(sub_score)
        sub_score = 0
        
    for i in tweet_score:
        if i < 0:
            negative = negative + 1
        if i > 0:
            positive = positive + 1
        if i == 0:
            neutral = neutral + 1
            

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
