
#!/usr/bin/python
# -*- coding: utf-8 -*-
import dash
import dash_leaflet as dl
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import dcc, html
import dash_mantine_components as dmc
import requests
import json

URL = "http://127.0.0.1:8000"

# Init the dropdown's list of cities
path_city = URL + "/city"
cities = json.loads(requests.request('GET', path_city).json())

# Load styles
#external_stylesheets = ['bootstrap.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=False)

# Main part of Dash App
app.layout = html.Div(
        [
	   html.Br(), 
            dbc.Row([
              dbc.Col([
                html.Img(src='assets/logo.png', height = '180px'), 
                html.Br(), html.Br(),
                dbc.Label("Durée du séjour"),
                dbc.Input(value = 1, type='number', min=1, max=7, step=1,id='input-days'),
                html.Br(),
                dbc.Label("Ville"),
                dcc.Dropdown(
                    placeholder='Choisissez une ville',
                    options=cities,
                    id='city-dropdown'
                ),
	            html.Br(),
                dbc.Label("Sélection des POI"),
                dcc.Dropdown(
                    id='poi-checklist',
                    multi=True),
                html.Br(),
                dbc.Row(
                    dmc.Button(
                        "Lancer l'itinéraire", 
                        variant="gradient", gradient={"from": "#50d8bc", "to": "#3c7282", "deg": 60}, 
                        id='btn-itinerary'),
                    className='d-grid gap-2 col-6 mx-auto'
                )
              ], width=4),
              dbc.Col(dl.Map(
                [
                    dl.TileLayer(), 
                    dl.GeoJSON(
                        #data=data,
                        zoomToBounds=True,
                        id='itinerary-geojson'
                    )],
                    center=(46.5, 2.2),
                    zoom=6,
                    style={'width': '800px', 'height': '700px', 'margin': "auto", 'display': 'block'},
                    id='main_map'
              ), width=8)
            ]),
        ], className='container-sm'
)

@app.callback(
    Output('poi-checklist', 'options'),
      Input('city-dropdown', 'value'),
      State('poi-checklist', 'options')
)
def update_checklist(city: str, options: list):
    """_summary_

    Args:
        city (str): city selected with dropdown component
        options (list): State handler for the list of POI to be displayed on the cheklist

    Raises:
        PreventUpdate: prevent the component to update
                        if city is not yet selected 

    Returns:
        POI label and values (list of dicts): list of dicts of 
                              POI to be displayed on the cheklist
    """

    if city !=None:
        _url = URL + "/poi/city/{value}".format(value=city)

        response = requests.request("GET", _url)
        poi_data = json.loads(response.json())
    else:
        raise PreventUpdate
        
    return [{ 'label': poi_data[i]['label'], 'value': poi_data[i]['identifier'] } \
               for i in range(len(poi_data))]

@app.callback(
    Output('itinerary-geojson', 'data'),
    [Input('btn-itinerary', 'n_clicks'),
      Input('poi-checklist', 'value'),
      Input('city-dropdown', 'value'),
      Input('input-days', 'value')],
)
def update_map(clicks: int, poi_identifiers: list, city: str, nb_days: int):
    """ Update the map with Itinerary information

    Args:
        clicks (int): number of clicks on Itinerary button
        poi_identifiers (list): list of POI identifiers
        city (str): city selected with dropdown component
        nb_days (_type_): number of days 

    Raises:
        PreventUpdate: prevent the component to update
                        if button is not clicked 

    Returns:
        data (GeoJSON): markers and polylines in geojson format
                        markes = POI and polylines = Itinerary paths
    """

    # Get triggered component
    # return its id
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    headers = {'Content-Type': 'application/json'}
    
    payload = json.dumps({
      "nb_days": nb_days,
      "identifiers": poi_identifiers
    })

    _url = URL + "/poi/city/{city}/itinerary".format(city=city)

    # If changed component id is the itinerary button
    # then call API 
    if 'btn-itinerary' in changed_id:
        response = requests.request(
            'GET', 
            _url,
            headers=headers, 
            data=payload
        )
        data = response.json()

        return data
    else:
        raise PreventUpdate

if __name__ == '__main__':
   app.run_server(debug=True,host="0.0.0.0", dev_tools_ui=False)   