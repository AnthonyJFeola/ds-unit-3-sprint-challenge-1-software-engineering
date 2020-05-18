from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    product = Product(name=(sample(ADJECTIVES,k=1) + sample(NOUNS,k=1)), price=randint(5,100), weight=randint(5,100), flammability=uniform(0.0,2.5))
    products.append(product)
    return products

def inventory_report(products):
    my_products = set(products)
    my_unique_products = len(list(my_products))
    print(f'Unique product names:', my_unique_products)


if __name__ == '__main__':
    inventory_report(generate_products())