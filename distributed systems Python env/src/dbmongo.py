from pymongo import MongoClient #pip install pymongo
#import certifi
import os

#Setear variable de entorno
#MONGO_URI = os.environ["MONGO_URI"]
MONGO_URI = "mongodb://mongo:8HFxnFYYUWFtL0WAdcui@containers-us-west-131.railway.app:6592"

#ca = certifi.where()

def dbConnection():
    try: 
        client = MongoClient(MONGO_URI)
        db = client['test']
    except :
        return False
    return db

def dbinfo():
    try: 
        client = MongoClient(MONGO_URI)
        jinfo = client.server_info()
    except:
        return False
    return jinfo.get('version')