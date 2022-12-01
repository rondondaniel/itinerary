# Etape 3 : Consommation des données

Cette étape consiste à appliquer un modèle de clustering et à calculer et  visualiser des trajets via Dash. Le dashboard a été couplé avec une API pour pouvoir utiliser la base de données MongoDB. 


## 1. Clustering avec l’algorithme K-means

L’objectif est de regrouper les POI en fonction de leur localisation (longitude, latitude). L’algorithme K-means est une méthode d’apprentissage non supervisée de clustering.

**Comment sont définis les clusters ?** 

Le centre d’un cluster correspond à la moyenne arithmétique de tous les points appartenant au cluster. Chaque point doit être plus proche du centre de son cluster que des centres des autres clusters. Dans Python, cette méthode peut être utilisée à l’aide de la librairie sklearn.

Avec cette méthode, le nombre de clusters k est défini à l’avance et doit être donné en entrée. Il est possible de le choisir de façon à optimiser le clustering, par exemple avec la méthode du coude mais pour ce projet, nous avons choisi de le faire correspondre avec la durée du séjour (k = nombre de jours). Chaque cluster, constitué par un ensemble de POI reliés par un itinéraire, correspond à une journée de voyage.

## 2. Calcul des itinéraires avec l'API OpenRouteService

L’API **OpenRouteService** fournit des services spatiaux en utilisant des données géographiques générées gratuitement par des utilisateurs à partir d’OpenStreetMap. Le service que nous avons utilisé s’appelle *Directions* et permet de renvoyer un itinéraire optimisé entre plusieurs lieux (deux ou plus) sous format GeoJSON. L’itinéraire peut s’effectuer en voiture, en vélo, à pied ou en fauteuil roulant.

**Fonctionnement du script python utilisé pour le calcul de l'itinéraire :**

* La fonction **get\_itinerary** récupère les POI correspondants à la commune choisie par l'utilisateur ainsi que la durée du séjour qui correspond au nombre de clusters. Cette fonction appelle la fonction **clustering\_kmeans** puis la fonction **get_paths**.

* La fonction **clustering_kmeans** réalise un clustering des POI en fonction de leur localisation en les séparant en k clusters. Elle retourne un DataFrame avec pour chaque label le cluster obtenu.

* La fonction **get_paths** appelle elle même la fonction **route** qui utilise l'API OpenRouteService pour calculer l'itinéraire optimal à partir des coordonnées des POI, puis crée deux objets : marker et polyline. L'objet marker contient les emplacements des POI tandis que polyline représente les routes reliant les POI d'un même cluster. La fonction renvoie un dictionnaire des deux objets en format GeoJSON qui est utilisé dans la construction de la map Dash Leaflet.

## 3. API

Cette interface entre le client et la logique métier est basée sur le framework FastAPI. Nous avons choisi ce framework car il est performant et rapide à prendre en main.

### API Enpoints

 <table>
  <tr>
    <th>Méthode</th>
    <th>Endpoint</th>
    <th>Authorisation</th>
    <th>Retourne</th>
  </tr>
  <tr>
    <td>GET</td>
    <td>/</td>
    <td>Non</td>
    <td>Permet de vérifier la santé de l'API</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/city</td>
    <td>Non</td>
    <td>Obtenir le nom de toutes les villes disponibles dans la base de données</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/poi/city/{city}</td>
    <td>Non</td>
    <td>Obtenir des informations sur les POI d'une ville</td>
  </tr>  
  <tr>
    <td>POST</td>
    <td>/poi/city/{city}/itinerary</td>
    <td>Non</td>
    <td>Obtenir des itinéraires optimisés</td>
  </tr>
</table> 