from flask import Blueprint, render_template, request, url_for, escape, redirect
from app.functions.auth import password_check
from app.functions.data_tools import data_getter

main_bl = Blueprint('main', __name__)

@main_bl.route("/", methods = ["GET", "POST"])
@main_bl.route("/index", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        status = password_check.username_and_password(username, password)
        if status == "L":
            return redirect(url_for("testt", username = username))
        elif status == "WP":
            return render_template("index.html", error = 1)
        elif status == "NO":
            return render_template("index.html", error = 2)
    else:
        return render_template("index.html", error = 0)