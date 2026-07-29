from flask import Flask

from .config import Config
from .logging_config import configure_logging
from .routes import bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    configure_logging(Config.LOG_LEVEL)

    app.register_blueprint(bp)

    return app