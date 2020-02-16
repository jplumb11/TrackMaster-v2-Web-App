from .login import main_bl

def init_app(app):
    app.register_blueprint(main_bl)