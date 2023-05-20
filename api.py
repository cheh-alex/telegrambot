import requests


def get_categories():
    url = "https://api.escuelajs.co/api/v1/categories"
    data = requests.get(url).json()
    return list(map(lambda l: l['name'], data))


def get_products(category):
    url = "https://api.escuelajs.co/api/v1/products"
    data = requests.get(url).json()
    return list(filter(lambda p: p['category']['name'] == category, data))