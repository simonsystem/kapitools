import bs4
import re
import time
import locale
import requests
import six

locale.setlocale(locale.LC_NUMERIC, "de_DE.UTF-8")

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

last_data, last_result = None, None

def calc_producing_rate(building, product, level, workers):
    assert isinstance(building, str)
    assert isinstance(product, str)
    assert isinstance(level, str)
    assert isinstance(workers, int)
    global last_data, last_result

    data = {
        "action": "send",
        "gebid": BUILDINGS[building],
        "level": LEVEL[level],
        "arbeiter": workers,
        "quali": 0,
        "zeitrechner": 0,
        "stunden": 1,
        "t_tag": int(time.time()),
        "t_std": 0,
        "t_min": 0,
        "submit": "rechnen"
    }
    url = "http://www.kapitools.de/regnum/prodmengen-rechner.php"

    if last_data != data:
        print("new")
        last_data = data
        last_result = requests.post(url, data=data)

    soup = bs4.BeautifulSoup(last_result.text)
    product_div_elem = soup.find(text=product)
    rate_string_elem = product_div_elem.parent.next_sibling.next_sibling.next_element
    return locale.atof(rate_string_elem)


