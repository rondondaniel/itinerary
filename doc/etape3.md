# Etape 3 : Consommation des données

## 1. API

Cette interface entre le client et la logique métier est basée sur le framework FastAPI. Nous avons choisi ce framework car il est performant et rapide à prendre en main. Afin d'approfondir le fonctionnement de l'API il est également possible de lire la [documentation dédiée à l'API](../src/api/README.md).

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

## 2. Clustering

En ce qui concerne la partie Machine Learning, nous nous sommes inspirés des articles ci-dessous :

* [Improving Itinerary Recommendations for Tourists Through Metaheuristic Algorithms: An Optimization Proposal](https://www.researchgate.net/publication/340909418_Improving_itinerary_recommen
dations_for_tourists_through_metaheuristic_algorithms_an_optimization_proposal)
* [Using Unsupervised Learning to plan a vacation to Paris: Geo-location clustering](https://towardsdatascience.com/using-unsupervised-learning-to-plan-a-paris-vacation
-geo-location-clustering-d0337b4210de) 