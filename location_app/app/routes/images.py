from flask import Blueprint, url_for, send_file

images_bl = Blueprint('images', __name__)

# @images_bl.route("/", methods = ["GET", "POST"])

    
@images_bl.route("/dot", methods = ["GET"])
def dot():
    return send_file('static/img/dot.svg')
