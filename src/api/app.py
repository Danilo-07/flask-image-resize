from flask import Flask

from .image_routes import image_bp


def create_app() -> Flask:
    flask_app = Flask(__name__)
    flask_app.register_blueprint(image_bp)

    return flask_app
