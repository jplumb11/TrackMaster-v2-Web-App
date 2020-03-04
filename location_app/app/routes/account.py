from flask import Blueprint, render_template, request, url_for, escape, redirect, session
from app.functions.data_tools import data_getter

acc_bl = Blueprint('acc', __name__)

@acc_bl.route("/", methods = ["GET", "POST"])
def index():
    return render_template("account_index.html")
