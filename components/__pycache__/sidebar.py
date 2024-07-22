import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app


from datetime import date, time
import plotly.express as px
import numpy as np
import pandas as pd  # Correção: pandas

layout = dbc.Col([
    html.H1('Mybudget', className="text-primary"),  # Correção: className
    html.P('By Caio Croccia', className="text-info"),  # Correção: className
    html.Hr(),
    # Secção de Perfil
    dbc.Button(id="botao-avatar",
               children=[html.Img(src='/assets/img_hom.png',
                                  id='avatar_change', alt='Avatar', className='perfil_name')],
               style={'background-color': 'transparent', 'border-color': 'transparent'})
])
