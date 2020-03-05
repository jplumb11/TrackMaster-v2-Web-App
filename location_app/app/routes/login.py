from flask import Blueprint, render_template, request, url_for, escape, redirect, session
from app.functions.data_tools import data_getter
from datetime import datetime

login_bl = Blueprint('login', __name__)

@login_bl.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
    return render_template("login/index.html")

@login_bl.route("/create_account", methods = ["GET", "POST"])
def create_account():
    if request.method == "POST":
        print(request.form)
    return render_template("login/create.html", today = datetime.today().strftime('%Y-%m-%d'))


@login_bl.route("/forgot_password", methods = ["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        print(request.form)
    return render_template("login/forgot.html")