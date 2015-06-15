import bs4
import re
import time
import requests
import os
import json

BUILDINGS = {
    "Holzfaeller": 11,
    "Waffenschmiede": 22,
    "Muehlenbaeckerei": 33,
    "Manufaktur": 1,
    "Fischerei": 9,
    "Steinbruch": 3,
    "Karawanserei": 25,
    "Schlachterei": 8,
    "Goldschmiede": 23,
    "Druckerei": 24,
    "Obstpflueckerei": 10,
    "Weberei": 2,
    "Viehzucht": 5,
    "Brauerei": 7,
    "Quellbrunnen": 4,
    "Schreinerei": 26,
    "Bauernhof": 6
}

LEVEL = {
    "Baron": 16,
    "Buerger": 7,
    "Buergermeister": 14,
    "Freier": 6,
    "Freiherr": 15,
    "Fuerst": 19,
    "Fuerstbischof": 20,
    "Graf": 17,
    "Handelsherr": 11,
    "Herzog": 18,
    "Kaufmann": 10,
    "Kraemer": 8,
    "Kurfuerst": 21,
    "Leibeigener": 5,
    "Patrizier": 13,
    "Ratsmitglied": 12,
    "Weber": 9
}

class ProductNotFoundError(Exception):
    pass

last_data, last_result = None, None
cache_path = os.getcwd() + "/kapicache.json"

def set_cache(path):
    global cache_path
    cache_path = path

def _load_cache():
    try:
        with open(cache_path) as cache_file:
            return json.load(cache_file)
    except IOError:
        return []

def _save_cache(data):
    with open(cache_path, "w") as cache_file:
        json.dump(data, cache_file)

def _get_producing_rate_from_file(building, product, level, workers, alternative):
    for l in _load_cache():
        if l[:5] == [building, product, level, workers, alternative]:
            return l[5]
    return None

def _write_producing_rate_to_file(building, product, level, workers, alternative, producing_rate):
    c = _load_cache()
    c.append([building, product, level, workers, alternative, producing_rate])
    _save_cache(c)

def _get_producing_rate_from_server(building, product, level, workers, alternative):
    global last_data, last_result
    tstamp = int(time.time())
    data = {
        "action": "send",
        "gebid": BUILDINGS[building],
        "level": LEVEL[level],
        "arbeiter": workers,
        "quali": 0,
        "zeitrechner": 0,
        "stunden": 1,
        "t_tag": 79200 + tstamp - tstamp % 86400,
        "t_std": 0,
        "t_min": 0,
        "submit": "rechnen"
    }

    url = "http://www.kapitools.de/regnum/prodmengen-rechner.php"
    is_same = last_data and all(data[k] == last_data[k] for k in data)
    if not is_same:
        last_data = data
        last_result = requests.post(url, data=data)

    soup = bs4.BeautifulSoup(last_result.text)
    table = soup.find("table", class_="listtable")

    encoded_product = re.sub(r"([AOUaou]e|sz)", ".+", product)
    alt_re = re.compile("^" + encoded_product + " $")
    nonalt_re = re.compile("^" + encoded_product + "$")

    product_string_elem = alternative and table.find(text=alt_re) \
                                      or table.find(text=nonalt_re)
    if product_string_elem is None:
        raise ProductNotFoundError(
            "Could not find product '{}' in building '{}'."
             .format(product, building)
        )
    rate_string_elem = product_string_elem.parent.next_sibling.next_sibling.next_element
    us_float_string = rate_string_elem.replace(".", "").replace(",", ".")
    return float(us_float_string)

def calc_producing_rate(building, product, level, workers, alternative=True):
    """Get the calcutated producing rate from the server or a local file."""

    assert isinstance(building, str)
    assert isinstance(product, str)
    assert isinstance(level, str)
    assert isinstance(workers, int)
    assert isinstance(alternative, bool)

    r = _get_producing_rate_from_file(building, product, level, workers, alternative)
    if r is None:
        r = _get_producing_rate_from_server(building, product, level, workers, alternative)
        _write_producing_rate_to_file(building, product, level, workers, alternative, r)
    return r
