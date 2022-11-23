from fastapi import FastAPI
from business_logic import Mongo, Itinerary
from pydantic import BaseModel
import pandas as pd
from bson.json_util import dumps

# Instanciate Business Logic
mongo = Mongo()
itinerary = Itinerary()

class Labels(BaseModel):
    labels: list[str] = []

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
    return {'API Status': 'Running',
            'MongoDB:': mongo.check()
    }

@api.get('/city', name="Get list of cities")
def get_city():
    """Get list of name of all cities into the database

    Returns:
        list: name of all cities into the database
    """
    return dumps(mongo.get_city())

@api.get('/poi/city/{city:str}', name="Get list of all POI for a city")
def get_poi(city:str):
    """Get all POI information from a city

    Args:
        city (str): name of the city

    Returns:
       json: A json list with all poi inforamtion
    """
    return dumps(mongo.get_poi_by_city(city), indent=2)

@api.get('/poi/city/{city:str}/itinerary', name="Get optimized itinearary paths")
def get_itinerary(city: str, labels:Labels):
    """Get all POI information from a city

    Args:
        city (str): name of the city

    Returns:
       json: A json list with all poi inforamtion
    """
    return itinerary.get_itinerary(city, labels)

@api.get('/poi/region/{region:int}', name="Get list of regions")
def get_poi(region:int):
    
    return region