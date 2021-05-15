from flask import Flask, Response, redirect, request, abort
from flask_login import LoginManager, UserMixin, \
    login_required, login_user, logout_user

app = Flask(__name__)

# config
app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

@app.errorhandler(400)
def page_not_found(e):
    return "Login failed", 400


# callback to reload the user object


if __name__ == "__main__":
    app.run()
