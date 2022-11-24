from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

# Load env variables from .env file
load_dotenv()

CONNECTION_STRING = os.getenv('CONNECTION_STRING')

class DataBase():
    """ Class Shared by other classes to communicate
        to Mongo database
    """    

    def check():
        """ Check health of the database
        Returns:
            response (dict): server info if connection is ok
                                or an error message if not.
        """        

        response = {'ok': 'No'}

        try:
            client = MongoClient(CONNECTION_STRING)
            response = client.server_info()
        except errors.ServerSelectionTimeoutError as err:
            response = err

        return response

    def get_poi():
        """ Get bulk information from the database
        Returns:
            clean_col (collection object): bulk information as 
                                            mongo collection object
        """     

        client = MongoClient(CONNECTION_STRING)
        voyage = client["voyage"]
        clean_col = voyage.clean_POI

        return clean_col