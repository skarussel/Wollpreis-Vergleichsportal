from bs4 import BeautifulSoup
import constants
import db


def parse_product(brand, name, availability=True, html=None):
    """
    Takes a html page, products brand and name to find properties, returns a Product object

    Parameters:
        html (str): content of the webpage
        brand (str): products brand
        name (str): products name
        availlability (bool): If the product is availlable (default: True)

    Returns:
        Product Object with properties price, ingredients and strength if availlability is True
    """
    price, ingredients, strength = None, None, None
    if (not availability):
        return db.Product(brand=brand, name=name, availability=availability, price=price, ingredients=ingredients, strength=strength)
    soup = BeautifulSoup(html, "html.parser")
    price = soup.find("span", {"class": "product-price-amount"}).text
    if (price):
        price = price.replace(",", ".")
        price = float(price)
    rows = soup.find("div", {"id": "pdetailTableSpecs"}
                     ).find("table").find_all("tr")

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if (cols[0] == constants.ZUSAMMENSTELLUNG):
            ingredients = cols[1]
        if (cols[0] == constants.NAEDELSTAERKE):
            strength = cols[1]

    return db.Product(brand=brand, name=name, availability=availability, price=price, ingredients=ingredients, strength=strength)
