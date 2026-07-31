import socket

from flask import Blueprint
from flask import jsonify
from prometheus_client import CONTENT_TYPE_LATEST
from prometheus_client import generate_latest

from .config import Config

bp = Blueprint("api", __name__)


@bp.route("/")
def home():
    return jsonify(
        {
            "application": Config.APP_NAME,
            "message": "Welcome to Kubernetes Lite Deploy",
            "version": Config.APP_VERSION,
        }
    )


@bp.route("/health")
def health():
    return jsonify(
        {
            "status": "healthy",
            "hostname": socket.gethostname(),
        }
    )


@bp.route("/ready")
def readiness():
    return jsonify({"status": "ready"})


@bp.route("/version")
def version():
    return jsonify(
        {
            "version": Config.APP_VERSION,
        }
    )


@bp.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }