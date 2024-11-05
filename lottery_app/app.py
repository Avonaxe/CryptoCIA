from flask import Flask, render_template, request, redirect, url_for
from lottery_app import LotteryApp

app = Flask(__name__)
lottery_app = LotteryApp()

@app.route("/")
def index():
    return render_template("index.html", players=lottery_app.players)

@app.route("/enter", methods=["GET", "POST"])
def enter():
    if request.method == "POST":
        player_name = request.form["player_name"]
        message = lottery_app.enter_lottery(player_name)
        return render_template("enter.html", message=message)

    return render_template("enter.html")

@app.route("/pick_winner")
def pick_winner():
    winner, message = lottery_app.pick_winner()
    return render_template("winner.html", winner=winner, message=message)

@app.route("/blockchain")
def blockchain():
    chain = lottery_app.get_blockchain()
    return render_template("blockchain.html", chain=chain)

if __name__ == "__main__":
    app.run(debug=True)
