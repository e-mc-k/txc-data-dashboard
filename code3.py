# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 09:30:54 2022

@author: Dell
"""

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app = Dash(__name__)
app.layout = html.Div([
    html.H1(children='Hello Dash', style={'textAlign': 'center'}),

    html.Div(children='''
        Dash: A web application framework for your data.
    ''', style={'textAlign': 'center'}),
    
    html.Br(),
    
    html.Div([
        html.Div([
            html.Label('Column 1', style={'textAlign': 'center'}),
            dcc.Graph(id='g1', figure=fig)
        ], className="four columns"),

        html.Div([
            html.Label('Column 2', style={'textAlign': 'center'}),
            dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="four columns"),

        html.Div([
            html.Label('Column 2', style={'textAlign': 'center'}),
            dcc.Graph(id='g3', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="four columns"),
    ], className="row"),
    
    html.Div([
        html.Label('Put Input 1 Here'),
        dcc.Input(id="input1", type="number", placeholder="", debounce=True),
        html.Label('Input 1 Squared Equals'),
        html.Output(id='output'),
        html.Br(),
        html.Label('Put Input 2 Here'),
        dcc.Input(id="input2", type="number", placeholder="", debounce=True),       
    ]),
])
 
@app.callback(
    Output("output", "children"),
    Input("input1", "value"),
)
def update_output(input1):
    try: 
        int(input1)
        x = input1**3
    except:
        x = 0
    return x    
    #return u'Input 1 {}'.format(input1)

# app.css.append_css({
#     'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
# })

if __name__ == '__main__':
    app.run_server(debug=True)