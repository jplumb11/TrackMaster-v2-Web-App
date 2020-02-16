from flask import Flask
from app import mqtt, routes


app = Flask(__name__)
app.config.from_envvar('MYAPP_SETTINGS')

mqtt.init_app(app)

routes.init_app(app)



