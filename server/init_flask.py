from flask import Flask
from flask_cors import CORS


def get_flask_app():
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}})
    return app
