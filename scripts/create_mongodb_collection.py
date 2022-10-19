from pymongo import MongoClient
from pprint import pprint
import json

# Make sure to have a MongoDB instance running
# with Docker : docker run -d -p 27017:27017 --name mongo mongo 

client = MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())

# Create a DB voyage
voyage = client["voyage"]

# Create a collection called POI
# voyage.drop_collection('POI') # Drop collection if already exists 
voyage.create_collection(name='POI')
print(voyage.list_collection_names())

def insert_data(collection):
    with open("data/index.json", 'r', encoding='utf-8') as f:
        df = json.load(f) #.decode('utf-8')
            
    for file_link in df['file']:
        with open('data/objects/' + file_link, "r") as json_file:
            data = json.load(json_file)
            col.insert_one(data) 

col = voyage.POI
insert_data(col) # takes about 20 minutes

# Show first document
pprint(list(col.find().limit(1)))

# Create new collection to flatten the POI collection
results = col.aggregate([
    { 
      '$project': { 
        'identifier': '$dc:identifier', 
        'label': {'$first':'$rdfs:label.fr'}, 
        'type': '$@type', 
        'description':{'$first':'$rdfs:comment.fr'},
        'review': '$hasReview.hasReviewValue.rdfs:label.fr',
        'image': {'$first':{'$first':{'$first':'$hasRepresentation.ebucore:hasRelatedResource.ebucore:locator'}}},
        'homepage': {'$first':{'$first':'$hasContact.foaf:homepage'}},
        'email':{'$first':{'$first':'$hasContact.schema:email'}}, 
        'tel':{'$first':{'$first':'$hasContact.schema:telephone'}},
        'code_commune': {'$first':{'$first':'$isLocatedAt.schema:address.hasAddressCity.insee'}},
        'code_dept':{'$first':{'$first':'$isLocatedAt.schema:address.hasAddressCity.isPartOfDepartment.insee'}},
        'commune':{'$first':{'$first':'$isLocatedAt.schema:address.schema:addressLocality'}}, 
        'code_postal':{'$first':{'$first':'$isLocatedAt.schema:address.schema:postalCode'}},
        'latitude':{'$first':'$isLocatedAt.schema:geo.schema:latitude'}, 
        'longitude':{'$first':'$isLocatedAt.schema:geo.schema:longitude'},
        'petsAllowed':{'$first':'$isLocatedAt.petsAllowed'}, 
        'reducedMobilityAccess':'$reducedMobilityAccess'
      } 
    }
])

# voyage.drop_collection('clean_POI') # Drop collection if already exists 
voyage.create_collection(name='clean_POI')
clean_col = voyage.clean_POI
clean_col.insert_many(list(results))

print(clean_col.count_documents(filter={}))
# 415k POI

# Show first documents
pprint(list(clean_col.find().limit(5)))