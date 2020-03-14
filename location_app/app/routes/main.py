from flask import (Blueprint, render_template,
                   url_for, redirect, session)
from app.functions.data_tools import data_getter


main_bl = Blueprint('main', __name__)

@main_bl.route("/")
def index():
    """
    Renders the main page with users locations and preffered view
    """
    _locations = data_getter.get_locations_for(session['username'])
    return render_template("main/index.html", 
                           locations = _locations,
                           advanced = session['advanced'])

@main_bl.route("/advanced")
def advanced():
    """
    Changes the preffered view and saves it in cookies
    """
    if session['advanced'] == 0:
        session['advanced'] = 1
    else:
        session['advanced'] = 0
    return redirect(url_for('main.index'))

@main_bl.route("/logout")
def logout():
    """
    Deletes users data from cookies and goes to the login page
    """
    session['username'] = ""
    return redirect(url_for('index.index'))