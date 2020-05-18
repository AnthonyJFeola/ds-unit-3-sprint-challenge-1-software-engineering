from random import randint, sample, uniform
from statistics import mean
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    for _ in list(range(num_products)):
        adj = sample(ADJECTIVES, k=1)
        noun = sample(NOUNS, k=1)
        random_name = adj[0] + ' ' + noun[0]
        random_price = randint(5,100)
        random_weight = randint(5,100)
        random_flammability = uniform(0.0, 2.5)
        product = Product(name=random_name, price=random_price, weight=random_weight, flammability=random_flammability)
        products.append(product)
    return products

def inventory_report(products):
    prod_names = []
    prod_price = []
    prod_weight = []
    prod_flammability = []
    for product in products:
        prod_names.append(product.name)
        prod_price.append(product.price)
        prod_weight.append(product.weight)
        prod_flammability.append(product.flammability)
    prod_names_unique = len(list(set(prod_names)))
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names:', prod_names_unique)
    print(f'Average price:', mean(prod_price))
    print(f'Average weight:', mean(prod_weight))
    print(f'Average flammability:', mean(prod_flammability))
    
if __name__ == '__main__':
    inventory_report(generate_products())