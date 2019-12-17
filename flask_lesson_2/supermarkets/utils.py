import json

def get_data_supermarkets():
    with open('DB/supermarkets.txt', 'r') as file:
        return json.load(file)

def add_data_supermarkets(form):
    supermarkets = get_data_supermarkets()
    supermarkets.append(form)
    with open('DB/supermarkets.txt', 'w') as file:
        json.dump(supermarkets, file)
