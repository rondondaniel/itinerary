from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())

voyage = client["test"]

# Create a collection called POI
#voyage.drop_collection('ONE') # Drop collection if already exists 
voyage.create_collection(name='ONE')
print(voyage.list_collection_names())