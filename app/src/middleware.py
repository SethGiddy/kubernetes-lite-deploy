import time
import uuid

from flask import g
from flask import request

from .metrics import (
    IN_PROGRESS,
    REQUEST_COUNT,
    REQUEST_LATENCY,
)


def register_middleware(app):

    @app.before_request
    def before_request():

        g.start_time = time.time()

        g.request_id = str(uuid.uuid4())

        IN_PROGRESS.inc()

    @app.after_request
    def after_request(response):

        latency = time.time() - g.start_time

        REQUEST_LATENCY.labels(
            request.method,
            request.path,
        ).observe(latency)

        REQUEST_COUNT.labels(
            request.method,
            request.path,
            response.status_code,
        ).inc()

        response.headers["X-Request-ID"] = g.request_id

        IN_PROGRESS.dec()

        return response