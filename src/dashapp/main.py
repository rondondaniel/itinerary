
import dash
import dash_leaflet as dl
import requests
import json

url = "http://127.0.0.1:8000/poi/city/Bordeaux/itinerary"

payload = json.dumps({
  "labels": [
    "La Cité du Vin",
    "Les Halles de Bacalan",
    "Bassins de Lumières",
    "Musée du Vin et du Négoce",
    "Jardin public",
    "Parc Bordelais",
    "Esplanade des Quinconces et le monument aux Girondins",
    "Grosse Cloche",
    "Place de la Bourse",
    "Pont de pierre",
    "Tour Pey-Berland",
    "Cathédrale Saint-André",
    "Porte Cailhau",
    "Le Puy-Paulin",
    "Le Canal des 2 Mers à vélo"
  ]
})

headers = {
  'Authorization': 'Basic admin:4dm1x',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()

app = dash.Dash()
app.layout = dl.Map(
    [
        dl.TileLayer(), 
        dl.GeoJSON(data=data)
    ],
    center=(
        44.844, -0.577
    ),
    zoom=10,
    style={
            'width': '1000px', 
            'height': '500px',
            'margin': "auto", 
            "display": "block"
        }
    )

if __name__ == '__main__':
   app.run_server(debug=True,host="0.0.0.0", dev_tools_ui=False)   