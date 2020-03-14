from flask import (Blueprint, render_template, request,
                   url_for, redirect, session)
from app.functions.auth.login import login
from app.functions.auth.create_profile import create_profile
from app.functions.auth.change_password import change_password
from datetime import datetime


DAYS = [i for i in range(1,32)]
MONTHS = [("January", 1), ("February", 2), 
          ("March", 3), ("April", 4), 
          ("May", 5), ("June", 6), 
          ("July", 7), ("August", 8),
          ("September", 9), ("October", 10), 
          ("November", 11), ("December", 12)]
this_year = int(datetime.today().strftime('%Y'))
YEARS = list(reversed([i for i in range(1900, this_year + 1)]))

login_bl = Blueprint('login', __name__)

@login_bl.route("/", methods = ["GET", "POST"])
def index():
    """
    Renders the login page, handles POST requests for logging in
    and displays errors on the page also takes the user to the
    main page after successful login
    """
    if request.method == "POST":
        _status = login(request.form)
        if _status == "success":
            session["username"] = request.form["username"]
            return redirect(url_for('main.index'))
        else:
            return render_template("login/index.html",
                                   status = _status)
    return render_template("login/index.html",
                           status = "0")


@login_bl.route("/create_account", methods = ["GET", "POST"])
def create_account():
    """
    Renders the login page, handles POST requests for creating
    an account and displays errors on the page also takes the user
    back to the login page after creating the account
    """
    if request.method == "POST":
        _status = create_profile(request.form)
        if _status == "success":
            return redirect(url_for('login.index'))
        else:
            return render_template("login/create.html",
                                   status = _status,
                                   time = [DAYS, MONTHS, YEARS])
    return render_template("login/create.html", 
                           status = "0",
                           time = [DAYS, MONTHS, YEARS])


@login_bl.route("/forgot_password", methods = ["GET", "POST"])
def forgot_password():
    """
    Renders the login page, handles POST requests 
    and displays errors on the page also takes the user back to 
    the login page after changing the password 
    """
    if request.method == "POST":
        _status = change_password(request.form)
        if _status == "success":
            return redirect(url_for('login.index'))
        else:
            return render_template("login/forgot.html", 
                                   status = _status,
                                   time = [DAYS, MONTHS, YEARS])
    return render_template("login/forgot.html",
                           status = "0",
                           time = [DAYS, MONTHS, YEARS])