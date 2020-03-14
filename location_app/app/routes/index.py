from flask import Blueprint, url_for, redirect, session


index_bl = Blueprint('index', __name__) 

@index_bl.route("/", methods = ["GET", "POST"])
def index():
    """
    If there is user data saved in cookies it goes to
    the main page otherwise it will go to the login page
    """
    user = session.get('username')
    session['advanced'] = 0
    if user:
        return redirect(url_for('main.index'))
    else:
        return redirect(url_for('login.index'))