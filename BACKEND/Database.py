from decouple import config

def get_database():
    from pymongo import MongoClient
    import pymongo
    CONNECTION_STRING = config('DATABASE_URL')

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    return client
