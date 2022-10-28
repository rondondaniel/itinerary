from pymongo import MongoClient
import pandas as pd
import json

# Business Logic MongoDB database
class Mongo:
    def __init__(self):
        self.connect_string = "mongodb://localhost:27017/"

    def get_poi(self):
        client = MongoClient(self.connect_string)
        voyage = client["voyage"]
        clean_col = voyage.clean_POI

        return clean_col
    
    def get_cities(self):
        cities = self.get_poi().distinct("commune")

        return cities

    def get_poi_by_city(self, city):
        df = pd.DataFrame(list(self.get_poi().find(filter={'commune': city})))
        df = df.drop(['_id','identifier','type','image', 'code_commune', 'code_dept', 'code_postal', 'latitude', 'longitude', 'review'], axis=1, errors='ignore')
        
        return df.to_dict(orient='rows')

if __name__ == '__main__':
    mongo = Mongo()

    print(json.dumps(mongo.get_poi_by_city("Paris")))