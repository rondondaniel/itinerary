# Etape 2 : Architecture de l'Organisation des données

## 1. Architecture choisie
Un exemple de l'architecture choisie est sur l'image ci-dessous. Sur cette étude de cas où l'utilisateur choisi une ville et une durée du voyage :

![Itinerary Use Case][def]

L'architecture est divisée en Ingress, Databases, Backend, Frontend, et finalement une UI.

### a) Ingress
Cette partie de l'architecture récupère les données de la source. Ceci se fait par l'intermédiaire d'un script, appelé [create_mongodb_collection.py][def3]. 

Ensuite, un deuxième script, [create_neo4j_graph_example.py][def4] , s'en charge de extraire et de filtrer les données nécessaires à la création de la base de données Neo4j.

### b) Databases
Comme évoqué ci-dessus, deux databases sont utilisées : MongoDB et Neo4j.

#### I. MongoDB : 
Ce type de base de données de documents a été choisie par sa simplicité. Étant donné que les fichiers récupérés de la source sont en format JSON, il a été relativement rapide et efficace d'alimenter la base de données MongoDB. La rapidité et la fixibilité d’accès sont deux points importants pour notre projet.

#### II. Neo4j :
Comme l'objective final est de fournir un itinéraire, la base de données de type « Graph » nous semble un choix évident. C'est pour cette raison qu'une base Neo4j est implémentée. Elle servira essentiellement à créer l'itinéraire à partir des entrées de l'utilisateurs.

### c) Backend
Le backend est constitué par une API et sa logique métier ("Business Logic") :

#### I. API :
L'API sert d'interphase entre les requêtes côté clients et la logique métier qui permettent de répondre à ces requêtes. On détaille le fonctionnement de cette API dans la [doc de l'étape 3][def6]

#### II. "Business Logic" :
La "Business Logic" ou logique métier fonctionne comme un "Service ». En réalité nous avons séparé la logique métier en deux microservices :
* Un microservice dédié à la gestion et la "consommation" de données stockés dans la base MongDB,
* et un autre microservice qui s'occupe de communiquer avec la base Neo4j.  

Les deux microservices peuvent communiquer entre eux.

### d) Frondend/UI
Le frontend est une application Dash. Cette application est sensée de communiquer avec l'API. Pour plus de détails concernant l'application Dash et son interaction avec l'utilisateur vous pouvez lire la [doc dédiée à l'app Dash][def7].

## 2. Fichiers implémentant les bases de données
Dans le répertoire "scripts" se trouve les fichiers permettant de charger les bases de données MongoDB et Neo4j (voir [Ingress][def5])

## 3. Fichier de requête
Nous n'avons pas de fichier de requêtes en soit. En revanche la consommation de données se fait via une API. Les requêtes à la base de données sont gérées par des classes (une par base données) encapsulées dans la business logic (pour plus de détails sur la consommation de données, lissez la [section Business Logic][def2] plus haut).

[def]: ./images/Intinerary_use_case_2.jpg
[def2]: #ii-business-logic
[def3]: ../scripts/create_mongodb_collection.py
[def4]: ../scripts/create_neo4j_graph_example.py
[def5]: #a-ingress
[def6]: ./etape3.md
[def7]: ../src/dashapp/README.md