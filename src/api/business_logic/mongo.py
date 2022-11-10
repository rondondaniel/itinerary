from pymongo import MongoClient
import pandas as pd
import json
from bson.json_util import dumps
import pprint as pp

# Business Logic MongoDB database
class Mongo:
    def __init__(self):
        self.connect_string = "mongodb://localhost:27017/"

    def check(self):
        response = {'ok': 'No'}

        try:
            client = MongoClient(self.connect_string)
            response = client.server_info()
        except pymongo.errors.ServerSelectionTimeoutError as err:
            response = err

        return response

    def get_poi(self):
        client = MongoClient(self.connect_string)
        voyage = client["voyage"]
        clean_col = voyage.clean_POI

        return clean_col
    
    def get_cities(self):
        cities = self.get_poi().distinct("commune")

        return cities

    def get_poi_by_city(self, city):
        cursor_poi = list(self.get_poi().find(filter={'commune': city}))
        poi = dumps(cursor_poi, indent=2)

        return  poi

    def get_itinerary(self, city, labels):
        return {'hello': city,
                'labels': labels
        }

if __name__ == '__main__':
    mongo = Mongo()

    pp.pprint(mongo.get_poi_by_city("Bordeaux"))