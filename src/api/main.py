#!/usr/bin/python
# -*- coding: utf-8 -*-
from fastapi import FastAPI,  HTTPException
from business_logic import Mongo, Itinerary
from pydantic import BaseModel
import pandas as pd
from bson.json_util import dumps

# Instanciate Business Logic
mongo = Mongo()
itinerary = Itinerary()

class ItineraryInput(BaseModel):
    # add nb_cluster payload variable
    nb_days: int
    identifiers: list[str] = []

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
    return {
        'API Status': 'Running',
        'MongoDB:': mongo.check()
    }

@api.get('/city', name="Get list of cities")
def get_city():
    """Get list of name of all cities into the database

    Returns:
        list: name of all cities into the database
    """

    try:
       cities = dumps(mongo.get_city())
    except:
        raise HTTPException(status_code=500, detail='Error getting the names of all cities into the database')

    return cities

@api.get('/poi/city/{city:str}', name="Get list of all POI for a city")
def get_poi(city:str):
    """Get all POI information from a selected city

    Args:
        city (str): name of the city

    Returns:
       json: A json list with all poi inforamtion
    """

    try:
        poi = dumps(mongo.get_poi_by_city(city), indent=2)
    except:
        raise HTTPException(status_code=500, detail='Error getting all POI information from a selected city')

    return poi

@api.get('/poi/city/{city:str}/itinerary', name="Get optimized itinearary paths")
def get_itinerary(city: str, inputs:ItineraryInput):
    """Get itinerary paths from POI information and a selected city

    Args:
        city (str): name of the city
        inputs (class ItineraryInput): BaseModel witn number of days and list of
                                        POI identifiers.
    Returns:
       json: A json list with all poi inforamtion
    """

    try:
        itinerary_paths = itinerary.get_itinerary(city, inputs)
    except:
        raise HTTPException(status_code=500, detail='Error getting itinerary paths from POI information and a selected city')

    return itinerary_paths