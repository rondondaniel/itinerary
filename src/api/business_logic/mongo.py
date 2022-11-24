from business_logic import DataBase

class Mongo:
    """ Class acting as micro-service to get
        basic information from mongo data base
    """  


    def __init__(self):
        pass

    def check(self):
        """ Check health of the database

        Returns:
            response (dict): server info if connection is ok
                                or an error message if not.
        """        
                
        response = DataBase.check()

        return response

    def get_poi(self):
        """ Get bulk information from the database

        Returns:
            clean_col (collection object): bulk information as 
                                            mongo collection object
        """     

        clean_col = DataBase.get_poi()

        return clean_col
    
    def get_city(self):
        """ Get a list of cities stored into the database

        Returns:
            cities (list): list of cities
        """        

        cities = self.get_poi().distinct("commune")

        return cities

    def get_poi_by_city(self, city: str):
        """ Get the list of POI's by a selected city

        Args:
            city (str): selected city

        Returns:
            poi (list): list of POI's in the database
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