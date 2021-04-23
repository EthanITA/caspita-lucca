import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

# Set up the app and point it to Vue
app = Flask(__name__, static_folder='../client/dist/', static_url_path='/')


# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route("/ping")
def ping():
    return "PING!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
