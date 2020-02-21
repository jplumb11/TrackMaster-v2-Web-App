from .main import main_bl
from .map import map_bl


def init_app(app):
    app.register_blueprint(main_bl)
    app.register_blueprint(map_bl, url_prefix="/map")