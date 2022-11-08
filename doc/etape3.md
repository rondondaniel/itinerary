# Etape : Consommation des données

## 1. API
Cette interphase entre le client et la logique métier est basée sur le framework FastAPI. Nous avons choisi ce framework car il est performant et rapide à prendre en main.

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
    <td>/city</td>
    <td>Non</td>
    <td>List of thoughts of the user</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/region</td>
    <td>Non</td>
    <td>The newly created thought</td>
  </tr>
</table> 

## 2. Clustering

### Bibliographie :
En ce qui concerne la partie Machine Learning, nous avons trouvé l'inspireation à partir des articles ci-dessous :
* https://www.researchgate.net/publication/340909418_Improving_itinerary_recommen
dations_for_tourists_through_metaheuristic_algorithms_an_optimization_proposal
* https://towardsdatascience.com/using-unsupervised-learning-to-plan-a-paris-vacation
-geo-location-clustering-d0337b4210de