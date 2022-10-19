from pymongo import MongoClient
from neo4j import GraphDatabase
from py2neo import Graph
import pandas as pd

# MongoDB client and collection
client = MongoClient("mongodb://localhost:27017/")
voyage = client["voyage"]
clean_col = voyage.clean_POI

# Run Neo4j with Docker :
# docker run --name neo4j -p7474:7474 -p7687:7687 -d --env NEO4J_AUTH=none neo4j

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "neo4j"))

def add_poi(rows):
   # Adds paper nodes to the Neo4j graph as a batch job.
   query = '''
   UNWIND $rows as row
   CREATE (p:Poi {identifier:row.identifier, label:row.label, localisation:point({latitude:row.latitude, longitude:row.longitude})}) 
   RETURN count(distinct p) as total
   '''
   with driver.session() as session:
    session.run('CREATE CONSTRAINT pois IF NOT EXISTS ON (p:Poi) ASSERT p.identifier IS UNIQUE')
    res = session.run(query, parameters = {'rows': rows.to_dict('records')})
  
results_df = pd.DataFrame(list(clean_col.find(filter={'code_commune':'64289'})))
print(results_df.shape) # 50
print(results_df.head())

results_df = results_df[['identifier', 'label', 'latitude', 'longitude']]
results_df = results_df.astype({'latitude':'float'})
results_df = results_df.astype({'longitude':'float'})
add_poi(results_df)

# Check the graph on http://localhost:7474/browser/ : MATCH(n) RETURN n;
# Delete the graph : MATCH (n) DETACH DELETE n;