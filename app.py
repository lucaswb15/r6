import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

pio.templates.default = "plotly_dark"


url = "https://raw.githubusercontent.com/lucaswb15/r6data/master/R6%20Data%20-%20Ranked.csv"
df = pd.read_csv(url)

#=============================================================================
#Kills per player
kills = df[['Game','Lucas Kills', 'Hans Kills', 'David Kills', 'Ryan Kills', 'Sam Kills']]

fig = make_subplots(rows=1, cols=5, shared_xaxes=True, shared_yaxes=True,
                    subplot_titles=('Lucas Kills','Hans Kills', 'David Kills','Sam Kills','Ryan Kills'))

fig.add_trace(go.Scatter(x=kills['Game'], y=kills['Lucas Kills']), row=1, col=1)
fig.add_trace(go.Scatter(x=kills['Game'], y=kills['Hans Kills']), row=1, col=2)
fig.add_trace(go.Scatter(x=kills['Game'], y=kills['David Kills']), row=1, col=3)
fig.add_trace(go.Scatter(x=kills['Game'], y=kills['Sam Kills']), row=1, col=4)
fig.add_trace(go.Scatter(x=kills['Game'], y=kills['Ryan Kills']), row=1, col=5)

fig.update_layout(showlegend=False,
        margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4))
#=============================================================================
#Assists per player
assists = df[['Game','Lucas Assists', 'Hans Assist', 'David Assists', 'Ryan Assists', 'Sam Assists']]

fig6 = make_subplots(rows=1, cols=5, shared_xaxes=True, shared_yaxes=True,
                    subplot_titles=('Lucas Assists','Hans Assist', 'David Assists','Sam Assists','Ryan Assists'))

fig6.add_trace(go.Scatter(x=assists['Game'], y=assists['Lucas Assists']), row=1, col=1)
fig6.add_trace(go.Scatter(x=assists['Game'], y=assists['Hans Assist']), row=1, col=2)
fig6.add_trace(go.Scatter(x=assists['Game'], y=assists['David Assists']), row=1, col=3)
fig6.add_trace(go.Scatter(x=assists['Game'], y=assists['Sam Assists']), row=1, col=4)
fig6.add_trace(go.Scatter(x=assists['Game'], y=assists['Ryan Assists']), row=1, col=5)

fig6.update_layout(showlegend=False,
        margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4))

#=============================================================================
#Deaths per player
Deaths = df[['Game','Lucas Deaths', 'Hans Deaths', 'David Deaths', 'Ryan Deaths', 'Sam Deaths']]

fig_d = make_subplots(rows=1, cols=5, shared_xaxes=True, shared_yaxes=True,
                    subplot_titles=('Lucas Deaths','Hans Deaths', 'David Deaths','Sam Deaths','Ryan Deaths'))

fig_d.add_trace(go.Scatter(x=Deaths['Game'], y=Deaths['Lucas Deaths']), row=1, col=1)
fig_d.add_trace(go.Scatter(x=Deaths['Game'], y=Deaths['Hans Deaths']), row=1, col=2)
fig_d.add_trace(go.Scatter(x=Deaths['Game'], y=Deaths['David Deaths']), row=1, col=3)
fig_d.add_trace(go.Scatter(x=Deaths['Game'], y=Deaths['Sam Deaths']), row=1, col=4)
fig_d.add_trace(go.Scatter(x=Deaths['Game'], y=Deaths['Ryan Deaths']), row=1, col=5)

fig_d.update_layout(showlegend=False,
        margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4))
#=============================================================================
#Map Count

map_count = df.Map.value_counts().rename_axis('map').reset_index(name='counts')
fig1 = px.bar(map_count, x='map', y='counts',
             color='map', title="Count of Maps Played")

#=============================================================================
#Start Count

start_count = df.Start_Pos.value_counts().rename_axis('Start_Pos').reset_index(name='counts')
fig2 = px.pie(start_count, values = 'counts', names = 'Start_Pos', title="Percentages of Starting Position")
#=============================================================================
#Round Wins
rw = df[['Wins']].sum()
rl = df[['Loses']].sum()

#=============================================================================
#Win Rate

wins_p = df['Outcome'].value_counts(normalize=True) * 100

fig3 = go.Figure(go.Indicator(
    mode = "number",
    value = wins_p[1],
    title = {'text':"Win Rate"},
    number = {'suffix': "%"},
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

#-============================================================================
#Total Games
wins_t = df['Outcome'].value_counts()

fig4 = go.Figure(go.Indicator(
    mode = "number",
    value = wins_t.sum(),
    title = {'text':"Total Games"},
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))
fig4.update_layout(showlegend=False,
                   margin=dict(
                   l=1,
                   r=0,
                   b=0,
                   t=0,
                   pad=0))

#=============================================================================
#Total Wins

fig5 = go.Figure(go.Indicator(
    mode = "number",
    value = wins_t[1],
    title = {'text':"Total Wins"},
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

#=============================================================================
#Melt for pie by players
kills_melt = kills
kills_melt = kills_melt.melt(id_vars=['Game'], value_vars=['Lucas Kills','Hans Kills', 'David Kills','Sam Kills','Ryan Kills'])
kills_pie = px.pie(kills_melt, values = 'value', names = 'variable', title="Percentages of Kills")

#=============================================================================
#Melt for pie by players
assists_melt = assists
assists_melt = assists_melt.melt(id_vars=['Game'], value_vars=['Lucas Assists','Hans Assist', 'David Assists','Sam Assists','Ryan Assists'])
assists_pie = px.pie(assists_melt, values = 'value', names = 'variable', title="Percentages of Assists")

#=============================================================================
#Melt for pie by players
deaths_melt = Deaths
deaths_melt = deaths_melt.melt(id_vars=['Game'], value_vars=['Lucas Deaths','Hans Deaths', 'David Deaths','Sam Deaths','Ryan Deaths'])
deaths_pie = px.pie(deaths_melt, values = 'value', names = 'variable', title="Percentages of Deaths")

#=============================================================================
external_stylesheets = ['https://codepen.io/unicorndy/pen/GRJXrvP.css','https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

colors = {
    'background': '#FFFFFF',

    'text': '#FFFFFF'
}
server = app.server
app.title=tabtitle
app.layout = html.Div(
    html.Div([
        
        
        html.Div([
            html.H1(children='R6 Dashboard',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']}),
        ], className="row"),
        #Top Row             
        html.Div([
            html.Div([
                dcc.Graph(
                    figure=fig4,
                    ),
                ],className='two columns'),
            html.Div([
                dcc.Graph(figure=fig3)
            ],className='two columns')
        ],className='row'), 
        #second row
        html.Div([
            html.Div([
                dcc.Graph(
                    figure=kills_pie,
                    style = {
                        'margins-right':'-10%'}
                    )
                ],className='four columns'),
            html.Div([
                    dcc.Graph(
                        figure=assists_pie
                        )
                ],className='four columns'),
            html.Div([
                    dcc.Graph(
                        figure=deaths_pie
                        )
                ],className='four columns'),
        ],className='row'),
        
        #third row
        
        html.Div([
            html.Div([
                    dcc.Graph(
                        id = 'Maps Played',
                        figure=fig1,
                        style = {'margin-right':'-6.5%'}),
                ], className='eight columns'),
            html.Div([
                    dcc.Graph(
                        id = "Starting Pos",
                        figure=fig2,
                        style = {
                            'margins-right':'-10%'})
                ],className='four columns')
        ],className='row'
        ),
        
        
        #Kills per player
        html.Div([
            dcc.Graph(
                id = 'Kills per Player',
                figure=fig),
        ],className="row"),
        #Assists per player
        html.Div([
            dcc.Graph(
                id="Assists per Player",
                figure=fig6)
        ],className='row'),
        #Deaths per player
        html.Div([
            dcc.Graph(
                id="Deaths per Player",
                figure=fig_d)
        ],className='row'),    

    ])
)

if __name__ == '__main__':
    app.run_server(debug=False)
