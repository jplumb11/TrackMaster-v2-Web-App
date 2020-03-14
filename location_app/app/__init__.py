from flask import Flask
from app import mqtt, routes


def make_app():
    """
    Makes the app object with the configuration from
    an environment variable and connects routes and mqtt
    to the app
    """
    app = Flask(__name__)
    app.config.from_envvar('MYAPP_SETTINGS')

    mqtt.init_app(app)

    routes.init_app(app)
    return app


