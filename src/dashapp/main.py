
import dash
import dash_leaflet as dl
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dcc, html
import requests
import json

url = "http://127.0.0.1:8000/poi/city/Bordeaux/itinerary"

# Deprecated, used for testing
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

get_cities = json.loads(requests.request('GET', 'http://127.0.0.1:8000/city').json())

response = requests.request('GET', url, headers=headers, data=payload)
data = response.json()

# Load styles
external_stylesheets = ['bootstrap.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.layout = html.Div(
        [
            html.H1(
                'Itineraires de Vacances', 
                style={
                  'textAlign': 'center'
                }, 
                className='h1'
            ),
            dbc.Row([
              dbc.Col([
                dcc.Dropdown(
                    options=get_cities,
                    id='city-dropdown'
                ),
                dcc.Checklist(
                    id='poi-checklist',
                ),
              ]),
              dbc.Col(dl.Map(
                [
                    dl.TileLayer(), 
                    dl.GeoJSON(data=data)
                ],
                center=(
                    44.844, -0.577
                ),
                zoom=12,
                style={
                    'width': '1000px', 
                    'height': '500px',
                    'margin': "auto", 
                    "display": "block"
                }
              ))
            ])
        ], className='container-sm'
)

@app.callback(
    Output('poi-checklist', 'options'),
    Input('city-dropdown', 'value')
)
def update_checklist(value):
    if value !=None:
        print("City:", value)

        _url = "http://127.0.0.1:8000/poi/city/{value}".format(value=value)

        response = requests.request("GET", _url)

    poi_list = json.loads(response.json())
    
    labels = []
    for i in range(len(poi_list)):
        labels.append(poi_list[i]['label'])

    print("labels:", labels)

    return labels

if __name__ == '__main__':
   app.run_server(debug=True,host="0.0.0.0", dev_tools_ui=False)   