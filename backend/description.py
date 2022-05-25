import json
from api.data_mongo.get_data_mongo import get_data
from bson import json_util

def description_product(product):
    res = get_data("description", {"Producto":product}, {'Descripcion':1,'_id':0})
    return res

def laboratory(product):
    res = get_data("description", {"Producto":product}, {'Laboratorio':1,'_id':0})
    return res

def use_product(product):
    res = get_data("description", {"Producto":product}, {'Uso':1,'_id':0})
    return res