from pymongo import MongoClient, errors

# Business Logic MongoDB database
class Mongo:
    """ Class acting as micro-service to get
        basic information from mongo data base
    """  


    def __init__(self):
        self.connect_string = "mongodb://localhost:27017/"

    def check(self):
        """ Check health of the data base

        Returns:
            response (dict): server info if connection is ok
                                or an error message if not.
        """        
        response = {'ok': 'No'}

        try:
            client = MongoClient(self.connect_string)
            response = client.server_info()
        except errors.ServerSelectionTimeoutError as err:
            response = err

        return response

    def get_poi(self):
        """ Get bulk information from the Database

        Returns:
            clean_col (collection object): bulk information as 
                                            mongo collection object
        """     

        client = MongoClient(self.connect_string)
        voyage = client["voyage"]
        clean_col = voyage.clean_POI

        return clean_col
    
    def get_city(self):
        """ Get a list of cities stored into the database

        Returns:
            cities (list): list of cities
        """        
        cities = self.get_poi().distinct("commune")

        return cities

    def get_poi_by_city(self, city: str):
        """_summary_

        Args:
            city (_type_): _description_

        Returns:
            _type_: _description_
        """        
        poi = list(self.get_poi().find(filter={'commune': city}))
        
        return  poi

    def get_poi_by_labels(self, city: str, labels: list):
        """ (not implemented yet)

        Args:
            city (str): _description_
            labels (list): _description_
        """        
        
        return