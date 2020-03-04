from flask import Blueprint, url_for, redirect, session

index_bl = Blueprint('index', __name__)

@index_bl.route("/", methods = ["GET", "POST"])
def index():
    user = session.get('username')
    if user:
        return redirect(url_for('main.index'))
    else:
        return redirect(url_for('login.index'))
    

