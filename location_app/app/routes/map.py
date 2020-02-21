from flask import Blueprint, render_template, request, session, url_for, escape, redirect
from app.functions.data_tools import data_getter

map_bl = Blueprint('map', __name__)

@map_bl.route("/", methods = ["GET", "POST"])
def index():
    return render_template("map_index.html")