import json
import logging
import sys


class JsonFormatter(logging.Formatter):

    def format(self, record):

        return json.dumps(
            {
                "time": self.formatTime(record),
                "level": record.levelname,
                "message": record.getMessage(),
            }
        )


def configure_logging(level="INFO"):

    handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(JsonFormatter())

    logging.basicConfig(
        handlers=[handler],
        level=level,
    )