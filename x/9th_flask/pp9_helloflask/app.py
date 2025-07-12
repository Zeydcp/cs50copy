from flask import Flask, render_template, request

COLOR = [
    'red',
    'blue'
]

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        color = request.form.get("color")
        if color not in COLOR:
            return render_template("failure.html")
        return render_template("color.html", color=color)