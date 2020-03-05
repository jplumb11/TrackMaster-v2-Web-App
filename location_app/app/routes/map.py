from flask import Blueprint, render_template, request, session, url_for, escape, redirect
from app.functions.data_tools import data_getter

map_bl = Blueprint('map', __name__)

@map_bl.route("/", methods = ["GET", "POST"])
def index():
    return render_template("map/index.html", 
                           locations = data_getter.get_map_locations_for(session['username']),
                           dates = data_getter.get_map_location_dates(session['username']))