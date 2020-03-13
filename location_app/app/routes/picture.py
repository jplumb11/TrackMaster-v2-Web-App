from flask import Blueprint, render_template, request, url_for, escape, redirect, session
from app.functions.data_tools import data_getter

picture_bl = Blueprint('picture', __name__)


@picture_bl.route("/", methods = ["GET"])
def index():
    return render_template("picture/index.html", 
                           user = session['username'])

