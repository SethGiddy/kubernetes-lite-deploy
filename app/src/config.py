import os


class Config:
    APP_NAME = os.getenv("APP_NAME", "devops-health-api")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")