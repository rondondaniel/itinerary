# Vacantions Itenerary API

## Stand Alone API
To run the API in standalone mode, use the command below:

```bash
/src/api $ uvicorn main:api --reload
```

## API Routes

### /
Let you check the API health

### /cities
Get the name of all cities in the database

### /poi/city/{city}
Get POI information from a city

### /poi/region/{region}
Get POI information from a whole region (not yet implemented in this version)

## Business Logic

### MongoDB dabase logic
Logic & query related to the MongoDB database can be run as standalone using this command:

```bash
/src/api/business_logic $ python3 -m mongo.py
```
The main class is called Mongo. Below its methods:

```python
class Mongo:
    def __init__(self)
 
    def get_poi(self)
 
    def get_cities(self)
  
    def get_poi_by_city(self, city)

    def get_poi_by_region(self, region)
```

### Neo4j database logic