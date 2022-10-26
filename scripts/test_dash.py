from pymongo import MongoClient
import pandas as pd
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output

# MongoDB client and collection
client = MongoClient("mongodb://localhost:27017/")
voyage = client["voyage"]
clean_col = voyage.clean_POI
communes = clean_col.distinct("commune")

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(id = 'dropdown', options = communes, value = None, placeholder="Choose a city"),
    dash_table.DataTable(pd.DataFrame().to_dict('records'), id='data-table', 
    style_data={'whiteSpace': 'normal', 'height': 'auto'},
    style_cell={'textOverflow': 'ellipsis','maxWidth': 0})
])

@app.callback(
    Output('data-table', 'data'),
    [Input('dropdown', 'value')]
)

def update_df(city):
    df = pd.DataFrame(list(clean_col.find(filter={'commune': city})))
    df = df.drop(['_id','identifier','type','image', 'code_commune', 'code_dept', 'code_postal', 'latitude', 'longitude', 'review'], axis=1, errors='ignore')
    # bug avec les variables sous forme de listes

    return df.to_dict(orient='rows')

if __name__ == '__main__':
    app.run_server(debug = True, host='0.0.0.0')