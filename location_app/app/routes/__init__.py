from .index import index_bl
from .main import main_bl
from .map import map_bl
from .login import login_bl
from .account import acc_bl

def init_app(app):
    app.register_blueprint(index_bl)
    app.register_blueprint(main_bl, url_prefix="/main")
    app.register_blueprint(map_bl, url_prefix="/map")
    app.register_blueprint(login_bl, url_prefix="/login")
    app.register_blueprint(acc_bl, url_prefix="/profile")