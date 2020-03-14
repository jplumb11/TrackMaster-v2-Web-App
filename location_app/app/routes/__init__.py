from .index import index_bl
from .main import main_bl
from .map import map_bl
from .login import login_bl
from .profile import prof_bl
from .average import average_bl
from .picture import picture_bl


def init_app(app):
    """
    Registers all blueprints to the app with
    the appropriate url prefix
    """
    app.register_blueprint(index_bl)
    app.register_blueprint(main_bl, url_prefix="/main")
    app.register_blueprint(map_bl, url_prefix="/map")
    app.register_blueprint(login_bl, url_prefix="/login")
    app.register_blueprint(prof_bl, url_prefix="/profile")
    app.register_blueprint(average_bl, url_prefix="/average")
    app.register_blueprint(picture_bl, url_prefix="/picture")