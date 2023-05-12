from pymongo import MongoClient

def getdb(name):
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client.get_database(name)

def BoD_db():
    BoD = getdb("BoD")
    return BoD

def BoD_users_db():
    BoD_users = getdb("BoD_users")
    return BoD_users
