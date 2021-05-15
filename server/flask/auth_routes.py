from flask import request
from flask_login import login_required, logout_user, login_user, UserMixin

from server.firebase.firestore import db
from server.flask import app as flask_app, login_manager
from server.utils import hash


@flask_app.route("/logout")
@login_required
def logout():
    logout_user()
    return "OK", 200


class User(UserMixin):
    def __init__(self, user_id):
        self.user_id = user_id


@flask_app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        password = request.args['password']
        if hash.check_password(password, db.get_login_hashed_password()):
            login_user(User(password))
            return "OK", 200
        else:
            return "Not Found", 404


@login_manager.user_loader
def load_user(userid):
    return User(userid)
