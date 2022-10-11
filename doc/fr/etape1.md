# Découverte des sources de données disponible

## Context
L’objectif du projet est la création d’une application permettant à un utilisateur de planifier ses vacances à l’aide de données en open source. En fonction des points d’intérêt choisis ainsi que de la durée du séjour, l’application lui propose un itinéraire détaillé optimisant son temps de voyage et de séjour.
Le projet peut être éventuellement amélioré en se basant également sur les catégories des lieux choisis, ou les évaluations de TripAdvisor ou les périodes de fermeture de la destination.

## Périmètre
* **Géographique** : National
* **Itinéraires** : pédestres, équestre et cyclables
* **POI** : tous, puis filtrés au niveau du rendu
* **Rendu** : itinéraire style citymapper  avec une carte et sélecteur de points d’intérêt.

## Datatourisme (www.datatourisme.fr)
DATAtourisme est un **dispositif national de collecte et de diffusion en open data des données institutionnelles relatives au recensement de l'offre touristique** : description des points d'intérêt et événements touristiques géolocalisés et qualifiés.

Porté par l’Etat de 2015 à janvier 2022, et piloté par ADN Tourisme depuis le 1er février 2022, il est né d’une coopération inédite avec les réseaux des offices de tourisme, des agences départementales et des comités régionaux du tourisme de **l’ensemble du territoire national**.

## POI
Un POI (Point of Interest) est un élément touristique qui se décompose en 4 sous-types différents :

* **Produit** : un objet touristique pouvant se consommer (ex: chambre d’hôtel, pratique d’activité, visite guidée, ...)
* **Itinéraire touristique** : itinéraire composé d’étapes formant un parcours
* **Fête et manifestation** : manifestations, festivals, exposition ou tout autre évènement ayant un début et une fin
* **Lieu d’intérêt** : lieu ayant un intérêt touristique (ex: site naturel, site culturel, village, restaurant, …)

Le site data.gouv met à disposition un export simplifié des données au format CSV des données de type : 
* **événement** (FMA), 
* **lieux** (PLACE),
* **visites et activités** (PRODUCT), 
* **itinéraires** (TOUR).
