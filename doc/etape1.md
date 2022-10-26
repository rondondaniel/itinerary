# Etape 1 : Découverte des sources de données disponibles

## 1. Contexte et objectif

L’objectif du projet est la création d’une application permettant à un utilisateur de planifier ses vacances à l’aide de données en open source, issues du site [datatourisme.fr](https://www.datatourisme.fr/).

En fonction des points d’intérêt choisis ainsi que de la durée du séjour, l’application lui propose un itinéraire détaillé optimisant son trajet. L'utilisateur aura également la possibilité de filtrer les résultats pour obtenir uniquement les POI qui peuvent accueillir des personnes à mobilité réduite ou des animaux.

**Rendu** : application Dash qui renvoie les points d'intérêts de la commune choisie, et calcule un itinéraire selon les points d’intérêt choisis et la durée du séjour.

Le projet peut être éventuellement amélioré en se basant également sur les catégories des lieux choisis, les évaluations de TripAdvisor ou les périodes de fermeture de la destination.

### Datatourisme

DATAtourisme est un **dispositif national de collecte et de diffusion en open data des données institutionnelles relatives au recensement de l'offre touristique** : description des points d'intérêt et événements touristiques géolocalisés et qualifiés.

Porté par l’Etat de 2015 à janvier 2022, et piloté par ADN Tourisme depuis le 1er février 2022, il est né d’une coopération inédite avec les réseaux des offices de tourisme, des agences départementales et des comités régionaux du tourisme de **l’ensemble du territoire national**.

### Points d'intérêts (POI)

Un POI (Point of Interest) est un élément touristique qui se décompose en 4 sous-types différents :

* **Produit** : un objet touristique pouvant se consommer (ex: chambre d’hôtel, pratique d’activité, visite guidée, ...)
* **Itinéraire touristique** : itinéraire composé d’étapes formant un parcours
* **Fête et manifestation** : manifestations, festivals, exposition ou tout autre évènement ayant un début et une fin
* **Lieu d’intérêt** : lieu ayant un intérêt touristique (ex: site naturel, site culturel, village, restaurant, …)

<u>Effectifs approximatifs par type de point d'intérêt :</u>

| Type de POI				 	| Effectif |
|-------------------------	|----------|
| Lieu 						| 334 k    |
| Itinéraire touristique	| 16 k     |
| Produit 					| 32 k     |
| Fête et manifestation 	| 58 k     |

## 2. Récolte des données

Notre application a pour périmètre la France entière et s'intéresse aux 4 sous-types de POI.

### a) Récolte via data.gouv (option 1)

Le site data.gouv met à disposition un export simplifié des données au format CSV des données de type : 

* **événement** (FMA), 
* **lieux** (PLACE),
* **visites et activités** (PRODUCT), 
* **itinéraires** (TOUR).

Il est possible de récupérer les données très simplement. Par exemple :

~~~python
import pandas as pd

# Lien du fichier csv
csv_link = "https://static.data.gouv.fr/resources/datatourisme-la-base-nationale-des-donnees-publiques-dinformation-touristique-en-open-data/20221004-034515/datatourisme-product-20221004.csv"

## Lecture du fichier csv
df = pd.read_csv(csv_link)
~~~

**Exemple de donnée collectée :**

* Nom\_du\_POI : <span style="color:Purple">L'HIPPOCAMPE</span>
* Categories\_de\_POI : <span style="color:Purple">http://schema.org/Apartment|https://www.datatourisme.fr/ontology/core#PlaceOfInterest|
https://www.datatourisme.fr/ontology/core#PointOfInterest|
https://www.datatourisme.fr/ontology/core#Product|
https://www.datatourisme.fr/ontology/core#Accommodation|
https://www.datatourisme.fr/ontology/core#AccommodationProduct|
https://www.datatourisme.fr/ontology/core#Apartment|
https://www.datatourisme.fr/ontology/core#RentalAccommodation|
https://www.datatourisme.fr/ontology/core#SelfCateringAccommodation|
http://schema.org/Accommodation|http://schema.org/LodgingBusiness|http://schema.org/Product</span>
* Latitude : <span style="color:Purple">43.401964	</span>
* Longitude : <span style="color:Purple">3.696181</span>
* Adresse\_postale : <span style="color:Purple">7 Rue André Portes</span>
* Code\_postal\_et\_commune : <span style="color:Purple">34200#Sète</span>
* Covid19\_mesures\_specifiques : <span style="color:Purple">L’accueil se fait sans contact physique et l’appartement est désinfecté après chaque location par des professionnels.</span>
* Covid19\_est\_en\_activite
* Covid19\_periodes\_d\_ouvertures\_confirmees
* Createur\_de\_la\_donnee	: <span style="color:Purple">OT ARCHIPEL DE THAU - SETE</span>
* SIT\_diffuseur	: <span style="color:Purple">Hérault Tourisme</span>
* Date\_de\_mise\_a\_jour : <span style="color:Purple">2022-08-05</span>
* Contacts\_du\_POI	: <span style="color:Purple">#+33 6 15 41 84 20#sgmarcastel@wanadoo.fr#|L'HIPPOCAMPE#+33 6 15 41 84 20#contact@location-sete.site#https://location-sete.site/</span>
* Classements\_du\_POI	: <span style="color:Purple">3 étoiles#Classement officiel des hébergements touristiques</span>
* Description	: <span style="color:Purple">L'HIPPOCAMPE T2 de 45m2 neuf au coeur de Sète! Appartement dans une rue piétonne, calme, climatisé et non fumeur de 45m2 entièrement rénové et NEUF. il est situé en plein cœur de Sète, au 2ème étage d'un immeuble qui en comporte 3. Sans ascenseur.</span>
* URI\_ID\_du\_POI : <span style="color:Purple">https://data.datatourisme.fr/32/ba0bbbe0-54e1-35fc-83d2-6ad1d8506e59</span>

Ces données ont pour avantage d'être facilement récupérables mais elles sont moins complètes et ne permettent pas de mettre à jour facilement la base de données (il n'est pas possible de récupérer uniquement les POI nouveaux ou modifiés).

### b) Récolte via le webservice (option 2)

L’accès à l’application « Diffuseurs » DATAtourisme est ouverte à tous. Un compte peut être ouvert par l’intermédiaire du formulaire présent sur le site [https://diffuseur.datatourisme.gouv.fr/](https://diffuseur.datatourisme.gouv.fr/). 

L’espace « *Flux* » permet de créer et consulter des flux de données. Un **flux** contient les données résultant de la requête configurée avec l’éditeur de requête, dans le format indiqué (JSON ou XML). Ces données sont récupérables en téléchargement manuel  et automatique. 

Il est possible de sélectionner uniquement certaines catégories de données et de sélectionner plus finement la couverture géographique souhaitée. Ici nous avons choisi de sélectionner toutes les catégories de données sur l’ensemble des régions françaises, au format JSON.

Le format d’export est au format ZIP, composé d’un fichier JSON par POI ainsi que d’un fichier d’index comprenant, pour chaque POI inclus dans l’export, sa date de mise à jour et le nom du fichier correspondant. Sur la base du fichier d’index, il est possible de récupérer la liste des POI qui ont été supprimés et ceux qui ont été ajoutés ou mis à jour.

Pour pouvoir télécharger ses flux au travers du webservice, l'utilisateur doit utiliser une clé d'API. Cette clé d’API s’obtient pour chaque application déclarée sur la plateforme via l’espace « *Applications* ».

## 3. Données collectées</u> 

Le **fichier d'index** comprend les informations suivantes :

* le label du POI,
* sa date de mise à jour,
* le nom du fichier JSON correspondant.

<u>Exemple :</u>

~~~
[
  {
    "label": "CAMPING MUNICIPAL",
    "lastUpdateDatatourisme": "2022-06-29T05:01:59.233Z",
    "file": "b/b6/10-b61c4900-716d-302c-8e61-b532ab9fda90.json"
  },
  {
    "label": "BOITE À MUSIQUE - BAM",
    "lastUpdateDatatourisme": "2022-06-28T09:07:51.628Z",
    "file": "b/b6/10-b6236807-276f-321b-ab2a-bc8495c231c0.json"
  },
  {
    "label": "ESCAPE GAME HALLOWEEN",
    "lastUpdateDatatourisme": "2022-10-09T04:04:47.605Z",
    "file": "b/b6/10-b62501e4-2771-3b6a-b876-0cb721bdcf4e.json"
  }
]
~~~

Un **fichier individuel d'un POI** peut contenir :

* l'identifiant du POI,
* son label,
* la catégorie de POI (voir la liste [ici](/src/categories.csv)),
* sa description,
* son classement,
* les informations de contact (homepage, email, tel),
* les informations de localisation (libellé et code de la commune, libellé et code du département, adresse postale, latitude, longitude)
* les horaires d'ouverture,
* si les animaux de compagnie sont autorisés,
* si un accès est prévu pour les personnes à mobilité réduite.

Certaines de ces informations ne sont pas présentes dans tous les fichiers individuels. De plus, d'autres informations sont disponibles mais ne nous ont pas semblé pertinentes.

<u>Exemple :</u> 
  
~~~
{
  "@id": "https://data.datatourisme.fr/13/b02a4b65-5ec3-3f80-8cd9-ea8af229cb5f",
  "dc:identifier": "705679",
  "@type": [
    "schema:LocalBusiness",
    "schema:Museum",
    "CulturalSite",
    "Museum",
    "PlaceOfInterest",
    "PointOfInterest"
  ],
  "rdfs:comment": {
    "fr": ["Rassemblant plus de 100 000 œuvres, la collection du Musée national d’art moderne / Centre de création industrielle constitue l’un des premiers ensembles mondiaux de référence pour l’art des XXe et XXIe siècles."]
  },
  "rdfs:label": {
    "fr": ["Centre Pompidou"]
  },
  "hasContact": [
    {
      "@id": "https://data.datatourisme.fr/7280b7ab-c5af-32a9-8f3d-cda259542aa2",
      "schema:email": ["accessibilite@contact-centrepompidou.fr"],
      "schema:telephone": ["+33 1 44 78 12 33"],
      "foaf:homepage": ["https://www.centrepompidou.fr/"]
    }
  ],
  "isLocatedAt": [
    {
      "@id": "https://data.datatourisme.fr/6f75561b-decf-36a6-b811-12fd0e8a385d",
      "schema:address": [
        {
          "@id": "https://data.datatourisme.fr/8f6497df-d15a-3a19-8bad-3efb755ae9c4",
          "schema:addressLocality": "Paris 4e Arrondissement",
          "schema:postalCode": "75004",
          "schema:streetAddress": ["Place Georges Pompidou"],
          "hasAddressCity": {
            "@id": "kb:75104",
            "@type": ["City"],
            "rdfs:label": {"fr": ["Paris 4e Arrondissement"]},
            "insee": "75104",
            "isPartOfDepartment": {
              "@id": "kb:France1175",
              "@type": ["Department"],
              "rdfs:label": {"fr": ["Paris"]},
              "insee": "75"
            }
          }
        }
      ],
      "schema:geo": {
        "@id": "https://data.datatourisme.fr/22799b49-9576-3945-8459-cfbbd53eb2f5",
        "schema:latitude": "48.860713",
        "schema:longitude": "2.352254",
        "@type": ["schema:GeoCoordinates"]
      },
      "schema:openingHoursSpecification": [
        {
          "@id": "https://data.datatourisme.fr/4b46e71e-f784-35c6-b1a7-9a88cf7e5b95",
          "schema:closes": "22:00:00",
          "schema:opens": "11:00:00",
          "schema:validFrom": "2022-01-01T00:00:00",
          "schema:validThrough": "2022-12-31T23:59:59",
          "@type": [
            "schema:OpeningHoursSpecification"
          ],
          "additionalInformation": {
            "fr": ["Musée + Expositions : 11h - 21h
            		Nocturnes : les jeudis jusqu'à 23h dans les espaces d'exposition du niveau 6 (galeries 1 et 2)
            		Atelier Brancusi : 14h - 18h
            		Galerie des enfants : 11h - 19h
            		Évacuation des espaces d'exposition et du Musée 10 min avant la fermeture
            		Clôture des caisses 1h avant la fermeture"]
          }
        }
      ]
    }
  ],
  "lastUpdate": "2022-06-02",
  "lastUpdateDatatourisme": "2022-10-13T05:37:45.202Z"
}
~~~