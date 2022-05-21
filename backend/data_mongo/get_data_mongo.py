from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
url = f"mongodb+srv://{username}:{password}@salud-ocular.kpvby.mongodb.net/test"
db = MongoClient(url).get_database("ProyectoFinal")

def get_data(collection, filter={}, project={"_id":0}, limit=0, skip=0):
    return list(db[collection].find(filter,project).limit(limit).skip(skip))