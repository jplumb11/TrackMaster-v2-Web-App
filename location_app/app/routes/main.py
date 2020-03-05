from flask import Blueprint, render_template, request, url_for, escape, redirect, session
from app.functions.data_tools import data_getter

main_bl = Blueprint('main', __name__)

@main_bl.route("/")
def index():
    return render_template("main/index.html", locations = data_getter.get_locations_for(session['username']))

@main_bl.route("/logout")
def logout():
    session['username'] = ""
    return redirect(url_for('index.index'))