import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Getting the currect date time
todays_date = datetime.datetime.now()
todays_date = todays_date.strftime("%Y-%m-%d %H:%M:%S")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""


    ''' Data pre processing '''

    # Query database for cash of a user
    positions = db.execute("SELECT DISTINCT ticker, price, shares, cash FROM positions JOIN users ON positions.id = users.id WHERE users.id = :id", id=session["user_id"])

    # Getting the users cash into a vairble
    cash_dic = db.execute("SELECT cash FROM users WHERE id=:id", id=session['user_id'])

    user_cash = 0

    for dick in cash_dic:
        user_cash = dick.get("cash")

    # Vairbles for the ungodly amount of lists we need
    tickers = []
    shares = []
    prices = []
    current_price = []
    names = []
    total_values = []
    PL = []
    liquidation_value = user_cash

    # Filling the lists tickers, shares, and prices with the indivduals data
    for position in positions:
        # Also getting the users cash
        user_cash = position.get("cash")
        # tickers shares prices
        tickers.append(position.get("ticker").upper())
        shares.append(position.get("shares"))
        prices.append(position.get("price"))

    ''' Combine all of the positions with the same tickers together '''

    # Vairbles for two while loops
    j = 0
    i = 0
    # Looping through the length of any of those 3 lists
    while i < len(tickers):
        print(i)
        # Looping through the lists
        while j < len(tickers):
            # Checking if the current list item is equal to any other item in the list
            if tickers[i] == tickers[j]:
                # Making sure the item isn't equal to itself
                if i == j:
                    # Incrementing the loop
                    j += 1
                    continue
                # Adding the duplicate tickers data together and deleting the duplicate
                del tickers[j]
                shares[i] += shares[j]
                del shares[j]
                prices[i] += prices[j]
                del prices[j]
                # Setting j back by one to account for the missing duplicate
                j -= 1

            # Incrementing the loop
            j += 1
        # Incrementing the loop
        i += 1
        # Clearing the loop
        j = 0

    ''' Looking up all the values in this new lists '''

    # Using the users tickers for "lookup"
    for ii in range(len(tickers)):
        # Adding the lookup return to a list of dictionaries
        ticker_dictionary = (lookup(tickers[ii]))
        # Adding the current price to a list
        current_price.append(ticker_dictionary.get("price"))
        # Adding the name to a list
        names.append(ticker_dictionary.get("name"))
        # Calculating and adding the profit and loss to a list
        PL.append((current_price[ii] * shares[ii]) - prices[ii])
        # Adding the total value of a stock to a list
        total_values.append((current_price[ii] * shares[ii]))

        # Formatting these to only show 2 decimal places
        prices[ii] = "{:.2f}".format(prices[ii])
        total_values[ii] = "{:.2f}".format(total_values[ii])
        PL[ii] = "{:.2f}".format(PL[ii])

        # Vairible for the users LV
        liquidation_value += float(total_values[ii])

    ''' Formating for the html '''

    # Formating LV and user cash
    liquidation_value = "{:.2f}".format(liquidation_value)
    user_cash = "{:.2f}".format(user_cash)

    # Adding CASH to the each of the tickers list
    tickers.append("CASH")

    # Adding the users cash to the end of total values
    total_values.append(user_cash)

    return render_template("index.html", len=len(tickers), tickers=tickers, names=names, shares=shares, current_price=current_price, total_values=total_values, PL=PL, liquidation_value=liquidation_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Getting the users input
        ticker = request.form.get("ticker")

        # Using the users input for "lookup"
        dic = (lookup(ticker))

        # Checking if nothing was found
        if dic == None:
            return apology("no ticker found", 403)

        # A vairble to store the string 'cash' in
        user_cash = 0
        # Query database for cash of a user
        cash_dic = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        # Transforming this pesky syntax to get just the cash value
        for e in cash_dic:
            user_cash = e.get("cash")

        # Calc overall price
        overall_price = float(dic['price']) * float(request.form.get("nof_shares"))

        # Calc the balance in the users account after the transaction
        after_purchase = float(user_cash) - overall_price

        # Ensuring the user has enough money
        if after_purchase < 0:
            return apology("not enough cash")

        # Adding data to positions
        db.execute("INSERT INTO positions (id, ticker, price, shares, total_shares) VALUES (:id, :ticker, :price, :shares, 0)", id=session["user_id"], ticker=ticker, price=overall_price, shares=request.form.get("nof_shares"))

        # Getting the total shares for the ticker being bought
        total_shares_dic = db.execute("SELECT shares FROM positions WHERE ticker = :ticker AND id = :id", id=session['user_id'], ticker=ticker)

        total_shares = 0
        for i in total_shares_dic:
            total_shares += i.get("shares")
        print(f"ts: {total_shares}")

        # Adding the total shares into the db
        db.execute("UPDATE positions SET total_shares = :total_shares WHERE ticker = :ticker AND id = :id;", id=session["user_id"], ticker=ticker, total_shares=total_shares)

        # Updating users
        db.execute("UPDATE users SET cash = :new_cash WHERE id=:id", new_cash=after_purchase, id=session['user_id'])

        # Updating History
        db.execute("INSERT INTO history (id, ticker, price, shares, date) VALUES (:id, :ticker, :price, :shares, :date)", id=session["user_id"], ticker=ticker, price=dic['price'], shares=request.form.get("nof_shares"), date=todays_date)

        return redirect("/")

    elif request.method == 'GET':

        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Query database for cash of a user
    transactions = db.execute("SELECT ticker, shares, price, date FROM history WHERE id = :id", id=session["user_id"])

    # Vairbles for the ungodly amount of lists we need
    tickers = []
    shares = []
    prices = []
    dates = []

    # Filling the lists tickers, shares, and prices with the indivduals data
    for transaction in transactions:
        # tickers shares prices
        tickers.append(transaction.get("ticker").upper())
        shares.append(transaction.get("shares"))
        prices.append(transaction.get("price"))
        dates.append(transaction.get("date"))


    return render_template("history.html", len=len(tickers), tickers=tickers, shares=shares, prices=prices, dates=dates)


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
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
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

        # Getting the users input
        ticker = request.form.get("ticker")

        # Using the users input for "lookup"
        dic = (lookup(ticker))

        # Checking if nothing was found
        if dic == None:
            return apology("no ticker found", 403)

        # Stripping the dictionary of it's keys
        dic = dic.values()

        return render_template("quoted.html", dic=dic, ticker=ticker)

    elif request.method == 'GET':

        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure password confirmation was submitted
        elif not request.form.get("password_confirmation"):
            return apology("must provide password confirmation", 403)

        # Checking if the username is taken
        rows = db.execute("SELECT username FROM users WHERE username=:username", username=request.form.get("username"))

        if len(rows) >= 1:
            return apology("username taken", 403)

        # Ensuring that the password matches password confirmation
        elif request.form.get("password") != request.form.get("password_confirmation"):
            return apology("password doesn't match password confirmation", 403)

        # Hash the password
        hashed_password = generate_password_hash(request.form.get("password"))

        # Add the username and password to db
        db.execute("INSERT INTO users (username, hash, cash) VALUES (:username, :password, 10000.00)", username=request.form.get("username"), password=hashed_password)

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    ''' Gathering all the tickers into a list '''

    # Getting all the tickers from a user
    tickers_dic = db.execute("SELECT DISTINCT ticker FROM positions WHERE id=:id", id=session['user_id'])

    # Alist for tickers
    tickers = []

    # Looping through each ticker and adding it to the list
    for dic in tickers_dic:
        tickers.append(dic.get('ticker').upper())



    if request.method == "POST":

        ''' Gettting the total shares of the selected ticker '''

        # Query database for the total shares of a user/ create a vairble for it
        total_shares_dic = db.execute("SELECT DISTINCT total_shares FROM positions WHERE id = :id AND ticker=:ticker", ticker=request.form.get("ticker_selected").lower(), id=session["user_id"])

        total_shares = 0

        for v in total_shares_dic:
            total_shares = v.get("total_shares")

        """ Making sure that the the user has enough shares to sell them """

        if total_shares < int(request.form.get("nof_shares")):
            return apology("not enough shares")

        ''' updating all the shares in the positions '''

        positions = db.execute("SELECT ticker, price, shares, position_id FROM positions WHERE id=:id", id=session["user_id"])

        # A vairble to hold the users shares he wants to sell
        shares_left = int(request.form.get("nof_shares"))

        # This is used to hold the value, when there isn't enough shares in a position to only sell from the one positoin
        rollover_shares = 0

        # Looping over each position
        for position in positions:

            # If there are no shares left then we sold them all, congrats
            if shares_left != 0:

                # Checking if this position is the ticker we want to sell
                if position.get("ticker").upper() == request.form.get("ticker_selected"):

                    rollover_shares = int(position.get("shares")) - shares_left

                    # If RS is bigger than zero then this position had enough to finsh the sale
                    if rollover_shares > 0:

                        # Update the various columns for this position
                        single_share_price = float(position.get("price")) / float(position.get("shares"))

                        db.execute("UPDATE positions SET price = :single_share_price WHERE position_id=:position_id", position_id = position.get("position_id"), single_share_price = single_share_price)

                        db.execute("UPDATE positions SET shares = :new_shares WHERE position_id=:position_id ", new_shares = rollover_shares, position_id = position.get("position_id"))

                        db.execute("UPDATE positions SET price = :overall_price WHERE position_id=:position_id", position_id = position.get("position_id"), overall_price = single_share_price * rollover_shares)

                    # if RS = 0 then we just delete the position
                    elif rollover_shares == 0:

                        db.execute("DELETE FROM positions WHERE position_id=:position_id", position_id = position.get("position_id"))

                    # if RS < 0 then we are going to delete this one but keep in mind that we have to find another positoin to finsih the sale
                    elif rollover_shares < 0:

                        # The number of shares we still have to sell after clearning the current positon
                        shares_left = abs(rollover_shares)

                        # Clearing RS
                        rollover_shares = 0

                        db.execute("DELETE FROM positions WHERE position_id=:position_id", position_id = position.get("position_id"))

            else:

                break

        ''' Updating total shares '''

        # Getting the total shares for the ticker being bought
        total_shares_dic = db.execute("SELECT shares FROM positions WHERE ticker = :ticker AND id = :id", id=session['user_id'], ticker=request.form.get("ticker_selected").lower())

        total_shares = 0
        for i in total_shares_dic:
            total_shares += i.get("shares")

        # Adding the total shares into the db
        db.execute("UPDATE positions SET total_shares = :total_shares WHERE ticker = :ticker AND id = :id;", id=session["user_id"], ticker=request.form.get("ticker_selected").lower(), total_shares=total_shares)


        ''' Updating a user's cash when they sell '''

        # Getting the users cash into a vairble
        cash_dic = db.execute("SELECT cash FROM users WHERE id=:id", id=session['user_id'])

        user_cash = 0

        for dick in cash_dic:
            user_cash = dick.get("cash")

        # Using the users input for "lookup"
        dic = (lookup(request.form.get("ticker_selected")))

        # getting the current price of stock
        current_price = dic.get("price")

        # Getting the overall price by muliplying it by the nof shares
        overall_price = current_price * float(request.form.get("nof_shares"))

        # Updating the users cash with the sell
        user_cash += overall_price

        # Putting it in the data base
        db.execute("UPDATE users SET cash = :new_cash WHERE id=:id", new_cash=user_cash, id=session['user_id'])

        # Updating History
        db.execute("INSERT INTO history (id, ticker, price, shares, date) VALUES (:id, :ticker, :price, :shares, :date)", id=session["user_id"], ticker=request.form.get("ticker_selected"), price=current_price, shares=-1 * int(request.form.get("nof_shares")), date=todays_date)


        return redirect("/")


    else:

        return render_template("sell.html", tickers=tickers)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
