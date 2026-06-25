

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password):
    # Initializing the MongoClient. This helps to access the MongoDB
    # databases and collections.

        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d/?authSource=admin' %
            (username, password, HOST, PORT)
        )
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create a method to return the next available record number for use in the create method
            
   # create a new document in the animals collection
    def create(self, data):
        """Insert a new document into the animals collection."""
        if data is not None:
            try:
                #insert document into MongoDB
                result = self.collection.insert_one(data)
                return result.acknowledged
            except Exception as e:
                print("Error inserting document:", e)
                return False
        else:
            return False

    # Read documents from the animals collection
    def read(self, query):
        """Query documents from the animals collection."""
        if query is not None:
            try:
                # find matching documents
                result = self.collection.find(query)
                return list(result)
            except Exception as e:
                print("Error reading documents:", e)
                return []
        else:
            return []
        # Update documents in the animals collection
    def update(self, query, new_values):
        """Update documents in the animals collection."""
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except Exception as e:
                print("Error updating documents:", e)
                return 0
        else:
            return 0

    # Delete documents from the animals collection
    def delete(self, query):
        """Delete documents from the animals collection."""
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Error deleting documents:", e)
                return 0
        else:
            return 0