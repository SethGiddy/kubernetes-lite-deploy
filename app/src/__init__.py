from flask import Flask

from .config import Config
from .logging_config import configure_logging
from .routes import bp
from .middleware import register_middleware


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    configure_logging(Config.LOG_LEVEL)

    register_middleware(app)

    app.register_blueprint(bp)

    return app