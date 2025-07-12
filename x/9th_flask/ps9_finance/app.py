import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from pytz import timezone
from re import search

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""

    # Retrieve stocks from database
    user_id = session["user_id"]
    stocks = db.execute("SELECT symbol, shares FROM owned WHERE owner_id = ?", user_id)

    total = 0
    for stock in stocks:
        temp = float(lookup(stock["symbol"])["price"])
        stock["price"] = temp
        stock["total"] = int(stock["shares"]) * temp
        total += stock["total"]

    if request.method == "POST":
        modified = request.form.getlist("mshares")
        print(modified)
        for idx, stock in enumerate(stocks):
            try:
                new_shares = int(modified[idx])
                old_shares = int(stock["shares"])
                symbol = stock["symbol"]
                price = lookup(symbol)["price"]
                cash = (
                    float(
                        db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0][
                            "cash"
                        ]
                    )
                    - (new_shares - old_shares) * price
                )

                if new_shares < 0:
                    return apology("must provide positive number of shares", 400)

                if cash < 0:
                    return apology("you're too poor for this purchase", 400)

                if new_shares != old_shares:
                    # modify the shares
                    db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)
                    db.execute(
                        "INSERT INTO history (person_id, symbol, shares, price, time) VALUES (?, ?, ?, ?, ?)",
                        user_id,
                        symbol,
                        new_shares - old_shares,
                        price,
                        datetime.now(timezone("Europe/Belfast")),
                    )

                    if not new_shares:
                        db.execute(
                            "DELETE FROM owned WHERE symbol = ? AND owner_id = ?",
                            symbol,
                            user_id,
                        )
                    else:
                        db.execute(
                            "UPDATE owned SET shares = ? WHERE symbol = ? AND owner_id = ?",
                            new_shares,
                            symbol,
                            user_id,
                        )

            except ValueError:
                return apology("must provide valid number of shares", 400)

        # Return to home page
        return redirect("/")

    # Send stocks to home page
    cash = float(db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"])
    total += cash
    return render_template("index.html", stocks=stocks, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrieve symbol value from buying page
        symbol = request.form.get("symbol")

        # Ensure symbol was submitted
        if not symbol:
            return apology("must provide symbol", 400)

        # Ensure validity of symbol
        valid = lookup(symbol)
        if not valid:
            return apology("must provide valid symbol", 400)

        try:
            # Ensure shares is a positive number
            bought_shares = int(request.form.get("shares"))
            if bought_shares < 1:
                return apology("must provide positive number of shares", 400)

            # Ensure user has enough cash
            user_id = session["user_id"]
            price = valid["price"]
            cash = (
                float(
                    db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0][
                        "cash"
                    ]
                )
                - bought_shares * price
            )
            if cash < 0:
                return apology("you're too poor for this purchase", 400)

            # Lock in purchase into table
            symbol = symbol.upper()
            owned_shares = db.execute(
                "SELECT shares FROM owned WHERE symbol = ? AND owner_id = ?",
                symbol,
                user_id,
            )
            if owned_shares:
                owned_shares = int(owned_shares[0]["shares"]) + bought_shares
                db.execute(
                    "UPDATE owned SET shares = ? WHERE symbol = ? AND owner_id = ?",
                    owned_shares,
                    symbol,
                    user_id,
                )

            else:
                owned_shares = bought_shares
                db.execute(
                    "INSERT INTO owned (owner_id, symbol, shares) VALUES (?, ?, ?)",
                    user_id,
                    symbol,
                    owned_shares,
                )

            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)
            db.execute(
                "INSERT INTO history (person_id, symbol, shares, price, time) VALUES (?, ?, ?, ?, ?)",
                user_id,
                symbol,
                bought_shares,
                price,
                datetime.now(timezone("Europe/Belfast")),
            )

            # See portfolio
            return redirect("/")

        # Ensure shares is a positive number
        except ValueError:
            return apology("must provide positive number of shares", 400)

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Send history to home page
    return render_template(
        "history.html",
        history=db.execute(
            "SELECT symbol, shares, price, time FROM history WHERE person_id = ?",
            session["user_id"],
        ),
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        symbol = request.form.get("symbol")

        # Ensure symbol was submitted
        if not symbol:
            return apology("must provide symbol", 400)

        # Ensure validity of symbol
        quote = lookup(symbol)
        if not quote:
            return apology("must provide valid symbol", 400)

        # Get stock quote
        return render_template("quoted.html", quote=quote)

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("quote.html")


def has_numbers(password):
    return any(char.isdigit() for char in password)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrieve values from registration page
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        # Ensure password was confirmed
        elif not confirmation:
            return apology("must confirm password", 400)

        # Ensure password and confirmation are the same
        elif password != confirmation:
            return apology("these passwords didn't match", 400)

        # Ensure username is unique
        elif db.execute("SELECT * FROM users WHERE username = ?", username):
            return apology("username already taken", 400)

        elif len(password) < 3:
            return apology("use at least 3 characters", 400)

        if not has_numbers(password):
            return apology("include at least one number in password", 400)

        elif not search("[^a-zA-Z0-9s]", password):
            return apology("include at least one symbol in password", 400)

        # Insert new user and password into table
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username,
            generate_password_hash(password),
        )

        # Return to login page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrieve symbol value from buying page
        symbol = request.form.get("symbol")

        # Ensure symbol was submitted
        if not symbol:
            return apology("must provide symbol", 400)

        # Ensure validity of symbol
        valid = lookup(symbol)
        if not valid:
            return apology("must provide valid symbol", 400)

        try:
            # Ensure shares is a positive number, set sold_shares to negative
            sold_shares = -int(request.form.get("shares"))
            if sold_shares > -1:
                return apology("must provide positive number of shares", 400)

            # Ensure seller owns this stock
            symbol = symbol.upper()
            owned_shares = db.execute(
                "SELECT shares FROM owned WHERE symbol = ? AND owner_id = ?",
                symbol,
                user_id,
            )
            if not owned_shares:
                return apology("you do not own this stock", 400)

            # Ensure seller owns enough shares
            owned_shares = int(owned_shares[0]["shares"]) + sold_shares
            if owned_shares < 0:
                return apology("you do not own that many shares of this stock", 400)

            # Sell the shares
            price = valid["price"]
            cash = (
                float(
                    db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0][
                        "cash"
                    ]
                )
                - sold_shares * price
            )
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)
            db.execute(
                "INSERT INTO history (person_id, symbol, shares, price, time) VALUES (?, ?, ?, ?, ?)",
                user_id,
                symbol,
                sold_shares,
                price,
                datetime.now(timezone("Europe/Belfast")),
            )

            if not owned_shares:
                db.execute(
                    "DELETE FROM owned WHERE symbol = ? AND owner_id = ?",
                    symbol,
                    user_id,
                )
            else:
                db.execute(
                    "UPDATE owned SET shares = ? WHERE symbol = ? AND owner_id = ?",
                    owned_shares,
                    symbol,
                    user_id,
                )

            # Return to home page
            return redirect("/")

        # Ensure shares is a positive number
        except ValueError:
            return apology("must provide positive number of shares", 400)

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template(
        "sell.html",
        stocks=db.execute("SELECT symbol FROM owned WHERE owner_id = ?", user_id),
    )


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Change password"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrieve values from registration page
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure password was submitted
        if not password:
            return apology("must provide new password", 400)

        # Ensure password was confirmed
        elif not confirmation:
            return apology("must confirm new password", 400)

        # Ensure password and confirmation are the same
        elif password != confirmation:
            return apology("these passwords didn't match", 400)

        elif len(password) < 3:
            return apology("use at least 3 characters", 400)

        if not has_numbers(password):
            return apology("include at least one number in password", 400)

        elif not search("[^a-zA-Z0-9s]", password):
            return apology("include at least one symbol in password", 400)

        # Ensure password is new
        user_id = session["user_id"]
        hash = db.execute("SELECT hash FROM users WHERE id = ?", user_id)
        if check_password_hash(hash[0]["hash"], password):
            return apology("you didn't choose a new password", 400)

        # Insert new password to users profile
        db.execute(
            "UPDATE users SET hash = ? WHERE id = ?",
            generate_password_hash(password),
            user_id,
        )

        # Return to homepage
        return redirect("/")

    return render_template("password.html")


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Add cash"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrieve values from registration page
        add = request.form.get("add")

        # Ensure they chose a positive number
        try:
            add = round(float(add), 2)
            if add < 0.01:
                return apology("No refunds", 400)

            # Add to account cash
            user_id = session["user_id"]
            db.execute(
                "UPDATE users SET cash = ? WHERE id = ?",
                float(
                    db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0][
                        "cash"
                    ]
                )
                + add,
                user_id,
            )

            # Return to home page
            return redirect("/")

        # Ensure user enters valid number
        except ValueError:
            return apology("Please provide a valid number", 400)

    # Get request
    return render_template("add.html")
