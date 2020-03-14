from flask import Blueprint, render_template, session
from app.functions.data_tools import data_getter


map_bl = Blueprint('map', __name__)

@map_bl.route("/", methods = ["GET", "POST"])
def index():
    """
    Renders the map page with all the data 
    thats needed for calculations
    """
    _locations = data_getter.get_map_locations_for(session['username'])
    _dates = data_getter.get_map_location_dates(session['username'])
    _weight = data_getter.get_weight_for(session['username'])
    _color = data_getter.get_color_for(session['username'])
    return render_template("map/index.html", 
                           locations = _locations,
                           dates = _dates,
                           weight = _weight,
                           color = _color)

