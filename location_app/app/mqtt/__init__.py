from flask_mqtt import Mqtt
from app.mqtt import mqtt_message_handler


def init_app(app):
    """
    Function to connect the mqtt to the app and setup
    on connect and on message callbacks
    """
    mqtt = Mqtt(app)

    @mqtt.on_connect()
    def handle_connect(client, userdata, flags, rc):
        mqtt.subscribe('owntracks/4009user/#')  #owntracks subscribing to mqtt

    @mqtt.on_message()
    def handle_mqtt_message(client, userdata, msg):
        mqtt_message_handler.getMsg(msg)
