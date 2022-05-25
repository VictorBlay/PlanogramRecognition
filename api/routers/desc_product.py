import json
from fastapi import APIRouter
from data_mongo.get_data_mongo import get_data
from bson import json_util

router = APIRouter()

@router.get("/{product}/Description")
async def description_product(product):
    res = get_data("description", {"Producto":product}, {'Descripcion':1,'_id':0})
    desc = []
    for i in res:
        for k, v in i.items():
            desc.append(v)
    return desc

@router.get("/{product}/Laboratory")
async def laboratory(product):
    res = get_data("description", {"Producto":product}, {'Laboratorio':1,'_id':0})
    lab = []
    for i in res:
        for k, v in i.items():
            lab.append(v)
    return lab

@router.get("/{product}/Use")
async def use_product(product):
    res = get_data("description", {"Producto":product}, {'Uso':1,'_id':0})
    use = []
    for i in res:
        for k, v in i.items():
            use.append(v)
    return use