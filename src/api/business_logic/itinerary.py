import pandas as pd
import os
from business_logic import DataBase
from sklearn.cluster import KMeans
import openrouteservice as ors
from dotenv import load_dotenv

# Load env variables from .env file
load_dotenv()

# Stores openrouteservice API Key
ORS_API_KEY = os.getenv('ORS_API_KEY') 

class Itinerary():
    """ Class acting as micro-service
        to calculate itineraries
    """    


    def __init__(self):
       pass
    
    def clustering_kmeans(self, data, nb_clusters: int):
        """ Method to determine clusters matching
            closest POI's

        Args:
            data (DataFrame): Coordinates, label, etc.
            nb_clusters (int): number of clusters to use 
                                for classification

        Returns:
            DataFrame: data dataframe + Cluster classification  
                        information using pandas concat method
        """        

        # Conversion de latitude et longitude en float
        data['longitude'] = data['longitude'].astype('float')
        data['latitude'] = data['latitude'].astype('float')

        km = KMeans(n_clusters=nb_clusters, random_state = 222)
        X = data[['longitude','latitude']].values
        predictions = km.fit_predict(X) 
        X_dist = 1000 * km.transform(X) ** 2

        return pd.concat([data.reset_index(drop=True), 
                          pd.DataFrame({'Cluster':predictions}),
                          pd.DataFrame({'sqdist':X_dist.sum(axis=1).round(2)})], axis=1)

    def route(self, coordinates, options=False):
        """ Calculate best route itinerary using 
            openrouteservice API

        Args:
            coordinates (DataFrame): POI's coordinates
            options (bool, optional): if True pass a options argument to
                                        openrouteservice's direction method. 
                                        Defaults to False.

        Returns:
            List: coordinates of the itineray paths
        """        

        # openrouteservice client
        client = ors.Client(ORS_API_KEY)
        
        if not options:
            route = client.directions(
                    coordinates=coordinates,
                    profile='foot-walking',
                    format='geojson',
                    options={"avoid_features": ["steps"]},
                    validate=False,
            )
        else:
            route = client.directions(
                    coordinates=coordinates,
                    profile='foot-walking',
                    format='geojson',
                    optimize_waypoints=True,
                    validate=False,
            )

        return route['features'][0]['geometry']['coordinates']
    
    def get_paths(self, clusters_data, nb_clusters: int):
        """ Method to construct intineraries and markers 
            in GeoJSON format

        Args:
            clusters_data (DataFrame): POI data including clusters information
            nb_clusters (int): number of classified clusters

        Returns:
            markers_geojson (dict): POI locations in points GeoJSON format
            polyline_geojson (dict): itineraries paths in polyline GeoJSON format
        """        

        marker = []
        polyline = []
        for nb_cluster in range(nb_clusters):
            cluster = clusters_data[clusters_data.Cluster == nb_cluster]
            cluster = cluster.sort_values('sqdist', ascending = False)
            cluster = cluster.reset_index(drop = True)

            coordinates = cluster[['longitude', 'latitude']].values.tolist()

            # 
            if len(coordinates)==1:
                # To Improve
                for c in coordinates:
                    marker.append(c) 
            elif len(coordinates) in [2,3]:
                # To Improve
                for c in coordinates:
                    marker.append(c) 
                polyline.append(self.route(coordinates))
            else:
                # To Improve
                for c in coordinates:
                    marker.append(c) 
                polyline.append(self.route(coordinates, options=True))
        
        # Dict to create markers and itinerary paths features in GeoJSON format
        # It could be replaced into a new method
        features = [{"type":"Feature","geometry":{"type":"Point","coordinates":m}} for m in marker]
        feature_polyline =  {"type":"Feature","geometry":{"type":"MultiLineString","coordinates":polyline}}
        features.append(feature_polyline)

        paths_geojson = {"type": "FeatureCollection", "features":features}
        
        return paths_geojson

    def get_itinerary(self, city: str, labels: list):
        """ Main method called from API

        Args:
            city (str): city to get POI's
            labels (list): POI names

        Returns:
            markers (dict): POI locations in points GeoJSON format
            paths (dict): itineraries paths in polyline GeoJSON format
        """  

        # Custers number hard coded. Should be an input.
        nb_clusters = 4

        df = pd.DataFrame(list(DataBase.get_poi().find(filter={'commune': city})))
        df = df.drop_duplicates(subset='label')
        
        data = df.loc[df.label.isin(labels.labels), ['identifier', 'label', 'longitude', 'latitude']]

        df_cluster = self.clustering_kmeans(data, nb_clusters)
        paths = self.get_paths(df_cluster, nb_clusters)

        return paths