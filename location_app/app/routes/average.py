from flask import Blueprint, render_template, request, url_for, escape, redirect, session
from app.functions.data_tools import data_getter

average_bl = Blueprint('average', __name__)


@average_bl.route("/", methods = ["GET"])
def index():
    return render_template("average/index.html", 
                           locations = data_getter.get_locations_for(session['username']))
