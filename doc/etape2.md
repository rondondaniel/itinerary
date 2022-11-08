# Etape 2 : Architecture de l'Organisation des données

## 1. Architecture choisie
Un exemple de l'architecture choisie est sur l'image ci-dessous. Sur cet étude de cas où l'utilisateur choisi une 

![Itinerary Use Case][def]



## 2. Fichiers implémentant les bases de données
Dans le repertoire "scripts" se trouve les fichiers permettant de charger les bases de données MongoDB et 

## 3. Fichier de requête
Nous n'avons pas de fichier de rêquete en soit. En revanche la consomation de données se fait via une API. Les request a la base de données sont gérées par des classes (une par base données) encapsulées dans le business_logic (pour plus de détails lire la [doc d'étape 3][def2]).

[def]: ./images/Intinerary_use_case_2.jpg
[def2]: etape3.md