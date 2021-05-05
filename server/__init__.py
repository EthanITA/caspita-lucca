import logging

from server.firebase import firestore
from server.init_flask import app as flask_app

logging.basicConfig(filename='server.log', level=logging.INFO)


def catch_internal_server_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(str(e))
            return "Internal Server Error", 500
    return wrapper
