from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = ""
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

CORS(app, resources={r'/*': {'origins': '*'}})