from flask import request

import server
from server.receipt import clothes

app = server.flask_app
db = server.firestore.db


@app.route("/api/ping")
def ping():
    return "PING!"


@server.catch_internal_server_error
@app.route("/private/login", methods=["POST"])
def private_login():
    return "OK", 200


@server.catch_internal_server_error
@app.route("/api/receipt/clothes/add", methods=["POST"])
def create_clothes_receipt():
    """
    Data must be sent with Content-Type: application/json and not empty
    {
        "supplier": string,
        "date": string,
        "payed": boolean,
        "products": array of json
    }
    where:
        "supplier" an arbitrary string which is the supplier name,
        "date" a string of the following format: "yyyymmdd",
        "payed" a boolean value,
        "products" an array of json that has the following fields:
            "item": string,
            "qty": int,
            "price": int (2.99 => 299), if float it'll be converted to int, in other words decimals would be truncated

    :return:
        201: created
        400: requirements not satisfied, ie. not valid type

    """
    try:
        clothes_receipt = clothes.Clothes(request.json)
    except (TypeError, ValueError) as e:
        server.logging.warning(e)
        return "Bad Request", 400

    db.collection('receipts').document('clothes').set(clothes_receipt.to_dict())
    server.logging.info(f"Created: {clothes_receipt}")
    return "Created", 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
