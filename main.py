import os

from flask import Flask
from flask_cors import CORS

"""
# Set up the app and point it to Vue
app = Flask(__name__, static_folder='client/dist/', static_url_path='/')
"""
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

"""
# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')
"""


@app.route("/api/ping")
def ping():
    return "PING!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
