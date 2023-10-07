import config
import json
import requests
import config as cfg

class ConvertException(Exception):
    pass

class APIError(Exception):
    pass

class Converse():
    def __init__(self, base, quote, amount):
        self.base = base
        self.quote = quote
        self.amount = amount

    @staticmethod
    def get_price(first: str, second: str, amount):
        r = requests.get("https://v6.exchangerate-api.com/v6/" + cfg.API_key + "/pair/" + str(cfg.list_of_values.get(first)) + "/" + str(cfg.list_of_values.get(second)))
        res = json.loads(r.text)
        if not(first in cfg.list_of_values.keys()) or not(second in cfg.list_of_values.keys()):
            raise ConvertException("вы указали валюты неверно")
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertException("Количесво введено неверно")
        if first == second:
            raise ConvertException("вы указали две одинаковых валюты")
        if res.get("result") != "success":
            raise APIError("не удалось отправить запрос")
        rate = res.get("conversion_rate")
        return (amount*float(rate))



