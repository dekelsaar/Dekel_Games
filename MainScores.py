from flask import Flask, render_template
from Utils import Path

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        score_file = open(Path("Scores.txt"), "r")
        score = score_file.read()
        return render_template('score.html', SCORE=score)
    except:
        return render_template('error.html', ERROR='Unknown Error')


app.run()
