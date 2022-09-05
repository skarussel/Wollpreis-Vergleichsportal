from urllib.request import urlopen
import csv
from parse import parse_product
import db


def init_product_names(path):
    """
    Read in Products from csv file and return the products as a list

        Parameters:
            path (str): path to a csv file, containing product names and brands seperated by ';'

        Returns:
            Products (List): 
    """
    products = []
    with open(path, newline='') as csvfile:
        productreader = csv.reader(csvfile, delimiter=";")
        for row in productreader:
            products.append(row)
    return products


def find_products(product_names):
    """
    Search for Products on Wollplatz Website, returns their properties as Product Objects 

        Parameters:
            product_names (list): list that contains a list of brand and names for each product

        Returns:
            Products (List): list of Product objects
    """
    products = []
    for product_name in product_names:
        try:
            url = create_url(*product_name)
            page = urlopen(url)
        except:
            print(f"{url} cannot be reached")
            product = parse_product(*product_name, availability=False)
        else:
            html = page.read().decode("utf-8")
            product = parse_product(*product_name, html=html)
        products.append(product)
    return products


def create_url(brand, name):
    """
    Takes a product brand and name, returns the url for the product on Wollplatz.de

    Parameter:
        brand (str): brand of the product
        name (str): name of the product

    Returns:
        URL (str): URL for product on Wollplatz.de
    """
    base_url = "https://www.wollplatz.de/wolle/"
    name = name.replace(" ", "-")
    return base_url + f"{brand}/{brand}-{name}".lower()


def save_to_file(products, path):
    """
    Save all Products from Database to a CSV File
    """
    with open(path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter=";")
        for product in products:
            writer.writerow(product.values())


if __name__ == "__main__":
    # remove all entries of Product Collection in Database
    db.delete_all()
    # get product_names from product_list.csv
    product_names = init_product_names('./product_list.csv')
    # find product properties from Wollplatz.de
    products = find_products(product_names)
    # insert products into Mongo Database
    db.insert_many(products)
    # save products in a CSV File
    save_to_file(products, "products.csv")
