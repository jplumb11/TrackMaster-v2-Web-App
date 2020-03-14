from flask import (Blueprint, render_template, request,
                   url_for, redirect, session)
from app.functions.data_tools import data_getter

prof_bl = Blueprint('prof', __name__)

@prof_bl.route("/", methods = ["GET", "POST"])
def index():
    """
    Renders the profile page with user data and handles
    changing of the weight and color through POST method
    """
    if request.method == "POST":
        data = request.form
        data_getter.update_data_for(session['username'], data)
    _user = data_getter.get_user_for(session['username'])
    _locations = data_getter.get_map_locations_for(session['username'])
    _dates = data_getter.get_map_location_dates(session['username'])
    return render_template("profile/index.html",
                           user = _user,
                           locations = _locations,
                           dates = _dates)


    