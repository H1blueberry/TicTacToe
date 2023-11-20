from flask import Flask, Blueprint, render_template, request, redirect, flash, url_for
views = Blueprint('views', __name__)

import sys
from website import tic_tac_toe as ttt
sys.setrecursionlimit(1000)

n = []
turn = 0
player1 = []
player2 = []
fields = ["upper_left", "upper_middle", "upper_right", "middle_left", "middle_middle", "middle_right", "bottom_left", "bottom_middle", "bottom_right"]
fields2 = fields
used = {}
error0 = ""


@views.route("/", methods=["GET", "POST"])
def home():
    global turn
    global error0
    if request.method == "GET":
        return render_template("website.html", p=used, error=error0)

    if request.method == "POST":
        if len(used) < 9:
            if turn == 0 or len(n) > 0:
                error0 = ""
                if len(n) > 0:
                     n.pop(0)
                field = request.form.get("field")
                if ttt.check_field(fields, player1, player2, field) == True:
                    player1.append(field)
                    fields2.remove(field)
                    used[field] = "X"
                    turn = 1

                    if ttt.check_win(player1) == True:
                        error0 = "Du hast gewonnen"
                        return render_template("website.html", p=used, error=error0)
                    render_template("website.html", p=used, error=error0)

                else:
                    error1 = "Wähle ein anderes Feld"
                    return render_template("website.html", p=used, error=error1)

                if len(used) < 9:
                    field = ttt.generate_field(fields2, player1, player2)
                    player2.append(field)
                    fields2.remove(field)
                    used[field] = "O"
                    turn = 0

                    if ttt.check_win(player2) == True:
                            error0 = "Computer hat gewonnen"
                            turn = 1
                            return render_template("website.html", p=used, error=error0)
                    return render_template("website.html", p=used, error=error0)

                else:
                    error0 = "Unentschieden"
                    return render_template("website.html", p=used, error=error0)
            else:
                print(n)
                return render_template("website.html", p=used, error=error0)
        else:
                    error0 = "Unentschieden"
                    turn = 1
                    return render_template("website.html", p=used, error=error0)


@views.route("/neu", methods=["POST"])
def neu():
     if request.method == "POST":
        global player1
        global player2
        global fields
        global fields2
        global used
        global n

        n = [1]
        player1 = []
        player2 = []
        fields = ["upper_left", "upper_middle", "upper_right", "middle_left", "middle_middle", "middle_right", "bottom_left", "bottom_middle", "bottom_right"]
        fields2 = fields
        used = {}
        error0 = ""
        return render_template("website.html", p=used, error=error0)
