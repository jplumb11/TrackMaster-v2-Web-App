from flask import Blueprint, render_template, request, url_for, escape, redirect, session
from app.functions.auth.login import login
from app.functions.auth.create_profile import create_profile
from app.functions.auth.change_password import change_password
from datetime import datetime

login_bl = Blueprint('login', __name__)

DAYS = [i for i in range(1,32)]
MONTHS = [("January", 1), ("February", 2), ("March", 3), ("April", 4), ("May", 5), ("June", 6), ("July", 7), ("August", 8), ("September", 9), ("October", 10), ("November", 11), ("December", 12)]
YEARS = list(reversed([i for i in range(1900, (int(datetime.today().strftime('%Y')) + 1))]))

@login_bl.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        _status = login(request.form)
        if _status == "success":
            session["username"] = request.form["username"]
            return redirect(url_for('main.index'))
        else:
            return render_template("login/index.html", status = _status)
    return render_template("login/index.html", status = "0")


@login_bl.route("/create_account", methods = ["GET", "POST"])
def create_account():
    if request.method == "POST":
        _status = create_profile(request.form)
        if _status == "success":
            return redirect(url_for('login.index'))
        else:
            return render_template("login/create.html", status = _status, days = DAYS, months = MONTHS, years = YEARS)
    return render_template("login/create.html", status = "0", days = DAYS, months = MONTHS, years = YEARS)


@login_bl.route("/forgot_password", methods = ["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        _status = change_password(request.form)
        if _status == "success":
            return redirect(url_for('login.index'))
        else:
            return render_template("login/forgot.html", status = _status, days = DAYS, months = MONTHS, years = YEARS)
    return render_template("login/forgot.html", status = "0", days = DAYS, months = MONTHS, years = YEARS)