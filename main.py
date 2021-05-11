from flask import Flask, render_template, redirect, request, url_for
from myLibrary import *

Check = Flask(__name__)


@Check.route("/", methods=["POST", "GET"])
def home():
    checkboard = Checkerboard()
    inst = checkboard.instruction
    if request.method == "POST":
        size = request.form.get("resize")
        mark = request.form.get("marking")
        checkboard.drawing(mark)
        checkboard.resize(size)
        return redirect(url_for("display"))
    else:
        return render_template("index.html", instruction=inst)


@Check.route("/display", methods=["POST", "GET"])
def display():
    Checkerboard().display()
    return render_template("display.html")


if __name__ == "__main__":
    Check.run(debug=True)