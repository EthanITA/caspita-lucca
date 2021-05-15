import logging
import os

from server.firebase import firestore
from server.flask import app, login_manager as flask_app, login_manager

logging.basicConfig(level=logging.INFO)

is_production = bool(os.getenv("is_gcloud", ''))


def catch_internal_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(str(e))
            return "Internal Server Error", 500

    return wrapper
