from flask import Blueprint, render_template, request, url_for, escape, redirect, session
from app.functions.auth import password_check
from app.functions.data_tools import data_getter

main_bl = Blueprint('main', __name__)

@main_bl.route("/", methods = ["GET", "POST"])
def index():
    return render_template("main_index.html", locations = data_getter.get_locations(), username = session['username'])