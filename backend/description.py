import requests

url ="https://pharmacorecode.herokuapp.com"

def description_product(product):
    return requests.get(url+f"/{product}/Description").json()[0]

def laboratory(product):
    return requests.get(url+f"/{product}/Laboratory").json()

def use_product(product):
    return requests.get(url+f"/{product}/Use").json()