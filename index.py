from dash import html, dcc
import dash 
form dash.dependencies import Input, Output
import dash._bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import sidebar


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
        ], md = 2)
    ])





], fluid=True,)