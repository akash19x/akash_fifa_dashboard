import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output , State
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

df = pd.read_csv("players_21.csv")

def drawspeed(player1):
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = df[df["short_name"] == player1]['movement_sprint_speed'].values[0],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "player sprint"}))

    return fig


fig5 = drawspeed('L. Messi')
fig6 = drawspeed('L. Messi')

# Use the hovertext kw argument for hover text
def draw2(player1, player2):
    colors = ['lightslategray',] * 5

    if df[df["short_name"] == player1]['height_cm'].values[0] > df[df["short_name"] == player2]['height_cm'].values[0]:
        colors[0] = 'crimson'
    else:
        colors[1] = 'crimson'

    x = [df[df["short_name"] == player1]['short_name'].values[0], df[df["short_name"] == player2]['short_name'].values[0]]

    y = [df[df["short_name"] == player1]['height_cm'].values[0], df[df["short_name"] == player2]['height_cm'].values[0]]

    fig2 = go.Figure(data=[go.Bar(x=x, y=y,
                hovertext=['27% market share', '24% market share', '19% market share']
                , marker_color=colors)])

    fig2.update_layout(title_text='.           Height cm (red is the talller)')
    return fig2

fig2 = draw2("L. Messi", "Song Yue")

import plotly.graph_objects as go


def draw(player1, player2):
    categories = ['passing', 'shooting', 'pace', 'physic', 'defending', 'dribbling']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[
            df[df["short_name"] == player1]['passing'].values[0],
            df[df["short_name"] == player1]['shooting'].values[0],
            df[df["short_name"] == player1]['pace'].values[0],
            df[df["short_name"] == player1]['physic'].values[0],
            df[df["short_name"] == player1]['defending'].values[0],
            df[df["short_name"] == player1]['dribbling'].values[0],

        ],
        theta=categories,
        fill='toself',
        name=player1,
        marker_color=['blue'],
        marker_line_color="blue",
        marker_line_width=6,
    ))

    fig.add_trace(go.Scatterpolar(
        r=[
            df[df["short_name"] == player2]['passing'].values[0],
            df[df["short_name"] == player2]['shooting'].values[0],
            df[df["short_name"] == player2]['pace'].values[0],
            df[df["short_name"] == player2]['physic'].values[0],
            df[df["short_name"] == player2]['defending'].values[0],
            df[df["short_name"] == player2]['dribbling'].values[0],

        ],
        theta=categories,
        fill='toself',
        name=player2,
        marker_color=['red'],
        marker_line_color="red",
        marker_line_width=6,
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=False,
                range=[0, 120]
            )),
        showlegend=True
    )

    return fig


fig = draw('Cristiano Ronaldo', 'Song Yue')
app = dash.Dash(__name__, external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([

    html.Div([

        html.Div([
            html.H1("Akash's Football Players' comparison."),
            html.Hr(),
        ], style={'height': '100px', 'width': '1450px', 'text-align': 'center'}),

        html.Div([

            html.Div([
                html.P("Choose a Player:"),
                dcc.Dropdown(
                    id="dropdown_1",
                    options=[
                        {'label': x, 'value': x}
                        for x in df['short_name']
                    ],
                    value='M. Salah',
                    clearable=False,
                )], className="six columns", style={'height': '100px', 'width': '200px'}),

            html.Div([
                html.P("Choose a Player:"),
                dcc.Dropdown(
                    id="dropdown_2",
                    options=[
                        {'label': x, 'value': x}
                        for x in df['short_name']
                    ],
                    value=df['short_name'][1],
                    clearable=False,
                )], className="six columns", style={'height': '100px', 'width': '200px', "float": "right"}),

        ], className="row"),

    ]),

    html.Div([

        html.Div([
            html.Img(src='/assets/333.png', width="300", height="300")], className="four columns"),

        html.Div([dcc.Graph(id='graph', figure=fig)], className="four columns", style={"background-color": "#e9c46a"}),

        html.Div([
            html.Img(src='/assets/2-removebg.png', width="300", height="300")], className="four columns",
            style={'height': '100px', 'width': '300px', "float": "right"}),

    ], className="row"),

    ###################################################

    html.Div([

        html.Div([
            html.P("Position"),
            html.P(children="kkkkkkkkk", id="1")

        ], className="two columns",
            style={'border': '1px solid', 'padding': '10px', 'box-shadow': '5px 10px 8px 10px #5747ff'}),

        html.Div([
            html.P("Value euro"),
            html.P(children="kkkkkkkkk", id="2")

        ], className="two columns",
            style={'border': '1px solid', 'padding': '10px', 'box-shadow': '5px 10px 8px 10px #5747ff'}),

        html.Div([
            html.P("Prefer foot"),
            html.P(children="kkkkkkkkk", id="3")

        ], className="two columns",
            style={'border': '1px solid', 'padding': '10px', 'box-shadow': '5px 10px 8px 10px #5747ff'}),

        html.Div([
            html.P("Prefer foot"),
            html.P(children="kkkkkkkkk", id="6")

        ], className="two columns",
            style={'border': '1px solid', 'padding': '10px', 'box-shadow': '3px 4px 2px 4px #e83131'}),

        html.Div([
            html.P("Value euro"),
            html.P(children="kkkkkkkkk", id="5")

        ], className="two columns",
            style={'border': '1px solid', 'padding': '10px', 'box-shadow': '3px 10px 8px 10px #e83131'}),

        html.Div([
            html.P("Position"),
            html.P(children="kkkkkkkkk", id="4")

        ], className="two columns",
            style={'border': '1px solid', 'padding': '10px', 'box-shadow': '3px 10px 8px 10px #e83131'}),

    ], className="row"),

    #############################################

    html.Div([

        html.Div([dcc.Graph(id='graph3', figure=fig5)], className="four columns",
                 style={"background-color": "#e9c46a"}),

        html.Div([dcc.Graph(id='graph2', figure=fig2)], className="four columns",
                 style={"background-color": "#e9c46a"}),

        html.Div([dcc.Graph(id='graph4', figure=fig6)], className="four columns",
                 style={"background-color": "#e9c46a"}),

    ], className="row"),

    ###################################################

    html.Div([

        html.Div([
            html.P("age"),
            html.P(children="kkkkkkkkk", id="7")

        ], className="two columns",
            style={'border': '1px solid', 'padding': '10px', 'box-shadow': '5px 10px 8px 10px #5747ff'}),

        html.Div([
            html.P("weight_kg"),
            html.P(children="kkkkkkkkk", id="8")

        ], className="two columns",
            style={'border': '1px solid', 'padding': '10px', 'box-shadow': '5px 10px 8px 10px #5747ff'}),

        html.Div([
            html.P("dribbling"),
            html.P(children="kkkkkkkkk", id="9")

        ], className="two columns",
            style={'border': '1px solid', 'padding': '10px', 'box-shadow': '5px 10px 8px 10px #5747ff'}),

        html.Div([
            html.P("dribbling"),
            html.P(children="kkkkkkkkk", id="13")

        ], className="two columns",
            style={'border': '1px solid', 'padding': '10px', 'box-shadow': '3px 4px 2px 4px #e83131'}),

        html.Div([
            html.P("weight_kg"),
            html.P(children="kkkkkkkkk", id="12")

        ], className="two columns",
            style={'border': '1px solid', 'padding': '10px', 'box-shadow': '3px 10px 8px 10px #e83131'}),

        html.Div([
            html.P("age"),
            html.P(children="kkkkkkkkk", id="11")

        ], className="two columns",
            style={'border': '1px solid', 'padding': '10px', 'box-shadow': '3px 10px 8px 10px #e83131'}),

    ], className="row"),

    #############################################

], style={"background-color": "#fcfcfc"})

@app.callback(
    Output(component_id='graph', component_property='figure'),
    Output(component_id='graph2', component_property='figure'),
    Output(component_id='graph3', component_property='figure'),
    Output(component_id='graph4', component_property='figure'),
    Input(component_id='dropdown_1', component_property='value'),
    Input(component_id='dropdown_2', component_property='value'),
    )
def update1(player1_name, player2_name):


    figuree = draw(player1_name, player2_name)

    figuree2 = draw2(player1_name, player2_name)

    speed1 = drawspeed(player1_name)

    speed2 = drawspeed(player2_name)


    return figuree, figuree2, speed1, speed2

@app.callback(
    Output(component_id='1', component_property='children'),
    Output(component_id='2', component_property='children'),
    Output(component_id='3', component_property='children'),
    Output(component_id='4', component_property='children'),
    Output(component_id='5', component_property='children'),
    Output(component_id='6', component_property='children'),
    Output(component_id='7', component_property='children'),
    Output(component_id='8', component_property='children'),
    Output(component_id='9', component_property='children'),
    Output(component_id='11', component_property='children'),
    Output(component_id='12', component_property='children'),
    Output(component_id='13', component_property='children'),
    Input(component_id='dropdown_1', component_property='value'),
    Input(component_id='dropdown_2', component_property='value'),
    )
def update2(player1_name, player2_name):

    x1 = df[df["short_name"] == player1_name]['team_position'].values[0]

    y1 = df[df["short_name"] == player1_name]['value_eur'].values[0]

    z1 = df[df["short_name"] == player1_name]['preferred_foot'].values[0]

    x2 = df[df["short_name"] == player2_name]['team_position'].values[0]

    y2 = df[df["short_name"] == player2_name]['value_eur'].values[0]

    z2 = df[df["short_name"] == player2_name]['preferred_foot'].values[0]

    xx1 = df[df["short_name"] == player1_name]['age'].values[0]

    yy1 = df[df["short_name"] == player1_name]['weight_kg'].values[0]

    zz1 = df[df["short_name"] == player1_name]['dribbling'].values[0]

    xx2 = df[df["short_name"] == player2_name]['age'].values[0]

    yy2 = df[df["short_name"] == player2_name]['weight_kg'].values[0]

    zz2 = df[df["short_name"] == player2_name]['dribbling'].values[0]

    return x1, y1, z1, x2, y2, z2, xx1, yy1, zz1, xx2, yy2, zz2


if __name__ == '__main__':
    app.run_server(debug=True,port=8049)