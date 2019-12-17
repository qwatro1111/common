import json

def get_data_products():
    with open('DB/products.txt', 'r') as file:
        return json.load(file)

def add_data_products(form):
    products = get_data_products()
    products.append(form)
    with open('DB/products.txt', 'w') as file:
        json.dump(products, file)
