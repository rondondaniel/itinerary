# Etape : Consommation des données

## 1. API
Cette interphase entre le client et la logique métier est basée sur le framework FastAPI. Nous avons choisi ce framework car il est performant et rapide à prendre en main. Afin d'approfondire sur le functionnement de l'API il est également possible de lire directement la [doc dédié à l'API][def].

### API Enpoints

 <table>
  <tr>
    <th>Verbe</th>
    <th>Endpoint</th>
    <th>Autho ?</th>
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
    <td>Obtenir des chemins itinéaires optimisés</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/poi/region/{region}</td>
    <td>Non</td>
    <td>Obtenir des informations sur les POI d'une région entière</td>
  </tr>
</table> 

## 2. Clustering

### Bibliographie :
En ce qui concerne la partie Machine Learning, nous avons trouvé l'inspireation à partir des articles ci-dessous :
* https://www.researchgate.net/publication/340909418_Improving_itinerary_recommen
dations_for_tourists_through_metaheuristic_algorithms_an_optimization_proposal
* https://towardsdatascience.com/using-unsupervised-learning-to-plan-a-paris-vacation
-geo-location-clustering-d0337b4210de

[def]: ../src/api/README.md