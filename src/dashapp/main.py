
import dash
import dash_leaflet as dl
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
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

#response = requests.request('GET', url, headers=headers, data=payload)
#data = response.json()

# Load styles
#external_stylesheets = ['bootstrap.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=False)
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
                dbc.Checklist(
                    id='poi-checklist',
                    labelCheckedClassName="text-success",
                    input_checked_style={'margin-right': '10px'}
                ),

              ], width=4),
              dbc.Col(dl.Map(
                [
                    dl.TileLayer(), 
                    #dl.GeoJSON(data=data)
                ],
                center=(
                    44.844, -0.577
                ),
                zoom=12,
                style={
                    'width': '800px', 
                    'height': '700px',
                    'margin': "auto", 
                    "display": "block"
                }
              ), width=8)
            ])
        ], className='container-sm'
)

@app.callback(
    Output('poi-checklist', 'options'),
    Input('city-dropdown', 'value'),
    State('poi-checklist', 'options')
)
def update_checklist(value, options):
    if value !=None:
        _url = "http://127.0.0.1:8000/poi/city/{value}".format(value=value)

        response = requests.request("GET", _url)

    poi_list = json.loads(response.json())

    return [{ 'label': poi_list[i]['label'], 'value': poi_list[i]['identifier'] } for i in range(len(poi_list))]

if __name__ == '__main__':
   app.run_server(debug=True,host="0.0.0.0", dev_tools_ui=False)   