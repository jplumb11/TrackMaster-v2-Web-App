from flask import Blueprint, render_template, request, url_for, escape, redirect, session
from app.functions.data_tools import data_getter

prof_bl = Blueprint('prof', __name__)

@prof_bl.route("/", methods = ["GET", "POST"])
def index():
    return render_template("profile/index.html",
                           user = data_getter.get_user_for(session['username']),
                           locations = data_getter.get_map_locations_for(session['username']),
                           dates = data_getter.get_map_location_dates(session['username']))
