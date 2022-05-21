import json
from data_mongo.get_data_mongo import get_data
from bson import json_util

def description_product(product):
    res = get_data("description", {"Producto":product}, {'Descripcion':1,'_id':0})
    return res