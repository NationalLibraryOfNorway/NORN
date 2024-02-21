from pymongo import MongoClient
from pymongo.collection import Collection

def connect_to_database(username: str, password: str, database: str = "norn", collection: str = "poems") -> Collection:
    """Connect to MongoDB database and return collection"""
    client = MongoClient(
        f"mongodb+srv://{username}:{password}@cluster0.wi1tz8b.mongodb.net/"
    )    
    return client[database][collection]