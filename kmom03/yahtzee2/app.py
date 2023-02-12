#!/usr/bin/env python3
"""
My first Flask app
"""

import traceback
import os
import re
from flask import Flask, render_template, request, redirect, url_for, session
#from src.die import Die
from src.hand import Hand

from src.rules import Rule
from src.rules import SameValueRule
from src.rules import Ones, Twos, Threes, Fours, Fives, Sixes
from src.rules import ThreeOfAKind, FourOfAKind, FullHouse, SmallStraight, LargeStraight, Yahtzee, Chance


app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

@app.route('/', methods=['GET', 'POST'])
def main():
    """ Main route """
    rules = [Ones(), Twos(), Threes(), Fours(), Fives(), Sixes(), ThreeOfAKind(), FourOfAKind(),
             FullHouse(), SmallStraight(), LargeStraight(), Chance(), Yahtzee()]
    
    hand_obj = Hand()
    
    if request.method == 'POST':
        print("in req meth")
        print("hand_obj")
        print(hand_obj)
        selected_rule = request.form.get("rule")
        selected_rule_obj = [r for r in rules if r.name == selected_rule][0]
        hand_obj.rule = selected_rule_obj
        session['last_dice'] = hand_obj.to_list()
        session['last_score'] = selected_rule_obj.points(hand_obj)
        session['total_score'] = session.get('total_score', 0) + session['last_score']
        return redirect(url_for('main'))

    my_dices = hand_obj.dice


    last_dice = session.get('last_dice')
    if last_dice:
        print("we in here yo yo")
        print(last_dice)
        last_hand_obj = Hand.from_list(last_dice)
        print("last_hand_obj")
        print(last_hand_obj)
        last_score = session.get('last_score')
        total_score = session.get('total_score')
    else:
        last_hand_obj = None
        last_score = None
        total_score = None

    return render_template("index.html", my_dices=my_dices, rules=rules, hand_obj=hand_obj,
                       last_dice=last_hand_obj, last_score=last_score, total_score=total_score)


@app.route('/reset', methods=['GET'])
def reset():
    _ = [session.pop(key) for key in list(session.keys())]
    session.clear()
    return redirect(url_for('main'))

@app.route("/init", methods=["GET"])
def init():
    """ Intialize values needed in session """
    hand = Hand()
    session["correct"] = game.get_correct_value()
    session["guesses"] = game.to_list()
    return redirect(url_for('guess'))

@app.route("/check", methods=["POST"])
def check():
    """ Check route """

    return redirect(url_for('main'))

@app.route("/about")
def about():
    """ About route """
    my_name = "David Palmgren"
    my_akronym = "Dapa22"

    return render_template("about.html", name=my_name, akronym=my_akronym)


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run()
