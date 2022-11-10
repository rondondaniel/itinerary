import pandas as pd
from business_logic import Mongo

class Itinerary():
    def __init__(self) -> None:
        pass

    def get_itinerary(self, city, labels):
        return {'hello': city,
                'labels': labels
        }