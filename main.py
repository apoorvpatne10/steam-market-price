import requests
from pprint import pprint
from currency_converter import CurrencyConverter

# Currency abbreviations
curAbbrev = {
    "USD": 1,
    "GBP": 2,
    "EUR": 3,
    "CHF": 4,
    "RUB": 5,
    "KRW": 16,
    "CAD": 20,
}


def get_item(appid, name, currency="USD"):
    url = "http://steamcommunity.com//market/priceoverview"
    market_item = requests.get(
        url,
        params={
            "appid": appid,
            "market_hash_name": name,
            "currency": curAbbrev[currency],
        },
    )
    return market_item.json()


def get_multiple(items, appid=440, currency="USD"):
    """Fetch multiple items using get_item()."""
    result = {}
    for item in items:
        result[item] = get_item(appid, item, currency)
    return result


def get_csgo_item(item, currency="USD"):
    """Fetches an item from CSGO. (Defaults the `appid` to 730)"""
    return get_item("730", item, currency)


name = "M4A4 | Neo-Noir (Field-Tested)"
item = get_csgo_item(name)

# Fetch price and convert to INR if needed
# c = CurrencyConverter()
# price = c.convert(float(item['lowest_price'][1:]), 'USD', 'INR')

pprint(item)
