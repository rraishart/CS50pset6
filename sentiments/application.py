from flask import Flask, redirect, render_template, request, url_for

import helpers
import os
import sys
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, 100)
    posScore = 0
    negScore = 0
    neuScore = 0
    
    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")  
    
    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)    
    
    for tweet in tweets:
        score = analyzer.analyze(tweet)
        if score > 0.0:
            posScore = posScore + 1
        elif score < 0.0:
            negScore = negScore + 1
        else:
            neuScore = neuScore + 1
    
    positive = posScore / (posScore + negScore + neuScore)
    negative = negScore / (posScore + negScore + neuScore)
    neutral = neuScore / (posScore + negScore + neuScore)


    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
