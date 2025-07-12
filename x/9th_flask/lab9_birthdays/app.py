import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        id = request.form.get("id")
        mid = request.form.get("mid")
        mname = request.form.get("mname")
        mmonth = request.form.get("mmonth")
        mday = request.form.get("mday")
        if id:
            try:
                id = int(id)
                db.execute("DELETE FROM birthdays WHERE id = ?", id)
            except ValueError:
                return redirect("/")
        elif name:
            try:
                month = int(month)
                day = int(day)
                if month in range(1, 13) and day in range(1, 32):
                    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
            except ValueError:
                return redirect("/")

        elif mname:
            try:
                mmonth = int(mmonth)
                mday = int(mday)
                if mmonth in range(1, 13) and mday in range(1, 32):
                    db.execute("UPDATE birthdays SET name = ?, month = ?, day = ? WHERE id = ?", mname, mmonth, mday, mid)

            except ValueError :
                return redirect("/")

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        rows = db.execute("SELECT * FROM birthdays;")
        return render_template("index.html", birthdays=rows)
