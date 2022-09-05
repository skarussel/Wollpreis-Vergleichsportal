import config
from mongoengine import *
from mongoengine.connection import disconnect


class Product(Document):
    brand = StringField()
    name = StringField()
    availability = BooleanField()
    price = FloatField(null=True)
    ingredients = StringField(null=True)
    strength = StringField(null=True)

    def values(self):
        return [self.brand, self.name, self.availability, self.price, self.ingredients, self.strength]


def establish_connection():
    "Connect to MongoDB database on Atlas, specified in config.py"
    username = config.username
    pw = config.pw
    con_str = config.connection_string
    db_url = f"mongodb+srv://{username}:{pw}@cluster0.{con_str}.mongodb.net/"
    connect("Wollservice", host=db_url)


def delete_all():
    "Delete all entries of Product Collection"
    establish_connection()
    Product.objects.delete()
    disconnect()


def insert_one(product):
    """
    Insert one Product into MongoDB Collection

    Parameter:
        product (Product)

    """
    establish_connection()
    product.save()
    disconnect()


def insert_many(products):
    """
    Insert many Products into MongoDB Collection

    Parameter:
        products (List: Products)

    """
    establish_connection()
    for product in products:
        product.save()
    disconnect()
