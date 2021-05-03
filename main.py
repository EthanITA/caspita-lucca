import server
app = server.get_flask_app()


@app.route("/api/ping")
def ping():
    return "PING!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
