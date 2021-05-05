import json

from server.utils.Json import JsonType
from server.utils.date import validate_date


class Clothes:
    def __init__(self, receipt_json: JsonType):
        """
        {
            "supplier": string,
            "date": string,
            "payed": bool,
            "products": array of json
        }
        where:
            "supplier" an arbitrary string which is the supplier name,
            "date" a string of the following format: "yyyymmdd",
            "products" an array of json that has the following fields:
                "item": string,
                "qty": int,
                "price": int (2.99 => 299), if float it'll be converted to int, in other words decimals would be truncated
        """
        data = json.loads(receipt_json)
        self.supplier, self.date, self.payed, self.products = (
            str(data["supplier"]),
            str(data["date"]),
            bool(data["payed"]),
            map(lambda product:
                {
                    "item": str(product["item"]),
                    "qty": int(product["qty"]),
                    "price": int(product["price"])
                },
                list(data["products"])
                )
        )
        if not validate_date(self.date):
            raise TypeError

    def to_dict(self):
        return {
            "supplier": self.supplier,
            "date": self.date,
            "payed": self.payed,
            "products": self.products,
        }

    def __str__(self):
        return str(self.to_dict())
