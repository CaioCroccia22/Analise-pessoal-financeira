from dash import html, dcc
import dash 
form dash.dependencies import Input, Output
import dash._bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import sidebar
from components import dashboards
from components import extratos


#: ===================== Layout ================ #
# Pagina principal
content = html.Div(id="Page-content")


#Layout principal do app
app.layout = dbc.Container(children=[
    # Abriu uma linha
    dbc.Row([
        # Abriu uma coluna para o projeto
        dbc.Col([
            dcc.Location(id='url'),
            # Instanciando component
            sidebar.layout
            # Nossa coluna vai ocupar 2 espaços de 12 do projeto
        ], md = 2),
        dbc.Col([
            content
        ], md = 10)
    ])




# Estabeleceu que o layout é fluido ou seja ele se espalha na página
], fluid=True,)

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname = '/' or pathname == '/dashboard':
        return dashboards.layout
    
    if pathname == '/extratos':
        return extratos.layout
    


if __name__ == '__main__':
    app.run_server(port=8051, dedug=True)