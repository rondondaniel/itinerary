from fastapi import FastAPI
from business_logic import Mongo
import pandas as pd
import json

# Load Business Logic for MongoDB database
mongo = Mongo()

api = FastAPI(
    title ='Vacancy Itenerary API',
    description="API is to query itenerary app databases.",
    version="0.1"
    )

@api.get('/', name="Check health")
def get_index():
    """Let you check the API health

    Returns:
        json:  message with API status
    """
    return {'API Status': 'Running'}

@api.get('/cities', name="Get list of cities")
def get_cities():
    """Get list of name of all cities into the database

    Returns:
        list: name of all cities into the database
    """
    return mongo.get_cities()

@api.get('/poi/city/{city:str}', name="Get list of POI for a city")
def get_poi(city):
    """Get POI information from a city

    Args:
        city (str): name of the city

    Returns:
        json: list of poi inforamtion
    """
    return json.dumps(mongo.get_poi_by_city(city))

@api.get('/poi/region/{region:str}', name="Get list of regions")
def get_poi(region):
    
    return region