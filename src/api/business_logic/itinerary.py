import pandas as pd
import os
from business_logic import Mongo
from sklearn.cluster import KMeans
import openrouteservice as ors
from dotenv import load_dotenv

# Load env variables from .env file
load_dotenv()

mongo = Mongo()

class Itinerary():
    def __init__(self):
       self.ORS_API_KEY = os.getenv('ORS_API_KEY')
    
    def clustering_kmeans(self, data, nb_clusters):    
        # Conversion de latitude et longitude en float
        data['longitude'] = data['longitude'].astype('float')
        data['latitude'] = data['latitude'].astype('float')

        km = KMeans(n_clusters=nb_clusters, random_state = 222)
        X = data[['longitude','latitude']].values
        predictions = km.fit_predict(X) 
        X_dist = 1000*km.transform(X)**2

        return pd.concat([data.reset_index(drop=True), 
                          pd.DataFrame({'Cluster':predictions}),
                          pd.DataFrame({'sqdist':X_dist.sum(axis=1).round(2)})], axis=1)

    def route(self, coordinates, options=False):
        client = ors.Client(self.ORS_API_KEY)
        
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
    
    def get_paths(self, clusters_data, nb_clusters):     
        
        marker = []
        polyline = []
        for nb_cluster in range(nb_clusters):
            cluster = clusters_data[clusters_data.Cluster == nb_cluster]
            cluster = cluster.sort_values('sqdist', ascending = False)
            cluster = cluster.reset_index(drop = True)

            coordinates = cluster[['longitude', 'latitude']].values.tolist()

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
        
        feature_markers = [{"type":"Feature","geometry":{"type":"Point","coordinates":m}} for m in marker]
        markers_geojson = {"type": "FeatureCollection", "features":feature_markers}

        polyline_geojson =  {"type": "FeatureCollection", "features":{"type":"Feature","geometry":{"type":"MultiLineString","coordinates":polyline}}}
        
        return markers_geojson, polyline_geojson

    def get_itinerary(self, city, labels):
        nb_clusters = 4
        df = pd.DataFrame(list(mongo.get_poi_by_city(city)))
        df = df.drop_duplicates(subset='label')
        
        data = df.loc[df.label.isin(labels.labels), ['identifier', 'label', 'longitude', 'latitude']]

        df_cluster = self.clustering_kmeans(data, nb_clusters)
        markers, paths = self.get_paths(df_cluster, nb_clusters)

        return markers, paths