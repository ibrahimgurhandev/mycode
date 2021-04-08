#!/usr/bin/python3
from flask import Flask
from flask import render_template

app = Flask(__name__)

# pull in the value of score as an int
@app.route("/scoretest/<score>")
def hello_name(score):
    # render the template with the value of score for marks
    # marks is a jinja var in the template
    try:
        string_int = int(score)
        return render_template("highscore.html", marks = string_int)
    except ValueError:
        return "You did not enter a number"

if __name__ == "__main__":
   app.run(host="localhost", port=2224)
