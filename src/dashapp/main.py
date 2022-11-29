
import dash
import dash_leaflet as dl
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dcc, html
import pandas as pd
import requests
import json

url = "http://127.0.0.1:8000/poi/city/Bordeaux/itinerary"

#nb_days = 4


# Homemade frontend store
df_store = pd.DataFrame(columns = ['identifier', 'label', 'longitude', 'latitude'])

headers = {
  'Authorization': 'Basic admin:4dm1x',
  'Content-Type': 'application/json'
}

get_cities = json.loads(requests.request('GET', 'http://127.0.0.1:8000/city').json())

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
                dbc.Input(
                    placeholder='Durée du séjour',
                    type='number',
                    id='input-days'
                ),
                dcc.Dropdown(
                    placeholder='Ville ...',
                    options=get_cities,
                    id='city-dropdown'
                ),
                dbc.Checklist(
                    id='poi-checklist',
                    labelCheckedClassName="text-success",
                    input_checked_style={
                      'margin-right': '10px'
                    },
                    class_name='mb-3',
                    style={
                    'height': '662px',
                    'margin': "auto", 
                    "display": "block",
                    "overflow-y": "scroll"
                }
                ),
              ], width=4),
              dbc.Col(dl.Map(
                [
                    dl.TileLayer(), 
                    dl.GeoJSON(
                        #data=data,
                        id='map-geojson'
                    )
                ],
                center=(
                    44.844, -0.577
                ),
                zoom=12,
                style={
                    'width': '800px', 
                    'height': '736px',
                    'margin': "auto", 
                    "display": "block"
                },
                id='main-map'
              ), width=8)
            ]),
            dbc.Row(
                dbc.Button(
                    "Lancer Itineraire", 
                    color='success',
                    id='btn-itinerary'
                ),
                className='d-grid gap-2 col-6 mx-auto'
            )
        ], className='container-sm'
)

@app.callback(
    Output('poi-checklist', 'options'),
    Input('city-dropdown', 'value'),
    State('poi-checklist', 'options')
)
def update_checklist(city, options):
    if city !=None:
        _url = "http://127.0.0.1:8000/poi/city/{value}".format(value=city)

        response = requests.request("GET", _url)

    poi_list = json.loads(response.json())

    return [{ 'label': poi_list[i]['label'], 'value': poi_list[i]['identifier'] } \
               for i in range(len(poi_list))]

@app.callback(
    Output('map-geojson', 'data'),
    [Input('btn-itinerary', 'n_clicks'),
      Input('poi-checklist', 'value'),
      Input('input-days', 'value')]
)
def update_map(click, values, nb_days):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    print(values)

    # Deprecated, used for testing
    payload = json.dumps({
      "nb_days": nb_days,
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

    if 'btn-itinerary' in changed_id:
        response = requests.request('GET', url, headers=headers, data=payload)
        data = response.json()

        return data
    else:
        return

if __name__ == '__main__':
   app.run_server(debug=True,host="0.0.0.0", dev_tools_ui=False)   