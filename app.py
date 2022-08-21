import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'Example_input_data.xlsx')
df = pd.read_excel(my_file)# replace with your own data source

# https://www.bootstrapcdn.com/bootswatch/
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )


# Layout section: Bootstrap (https://hackerthemes.com/bootstrap-cheatsheet/)
# ************************************************************************
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1("Bootstrap Dashboard",
                        className='text-center text-primary mb-4'),
                width=12)
    ),
    dbc.Row([
        dbc.Col([
            html.P("Applications overview:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='names', options=[{'label': 'STATUS', 'value': 'STATUS'}, {'label': 'RESULT', 'value': 'ACTIVE'},
             {'label': 'LABEL', 'value': 'LABEL'}],
                value='STATUS', clearable=False
        ),
            dcc.Graph(id='pie-graph', figure={}),
        ], #width={'size':4, 'offset':0, 'order':1},
           xs=12, sm=12, md=12, lg=4, xl=4
        ),
        dbc.Col([
            html.P("Company info found in list:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='names1', options=[{'label': 'found in list_1', 'value': 'found in list_1'}, {'label': 'found in list_2', 'value': 'found in list_2'}, {'label': 'found in list_3', 'value': 'found in list_3'}],
                value='found in CoC list', clearable=False
        ),
            dcc.Graph(id='pie-graph1', figure={}),
        ], #width={'size':4, 'offset':0, 'order':2},
           xs=12, sm=12, md=12, lg=4, xl=4
        ),
        
        dbc.Col([
            html.P("Top ten applicants:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-dpdn3', multi=True, 
            value=['Type_1', 'Type_2'], options=[{'label':x, 'value':x}
                                  for x in sorted(df['ORG_TYPE'].unique())]
            ),
            dcc.Graph(id='line-fig3', figure={})
        ], #width={'size':4, 'offset':0, 'order':3},
          xs=12, sm=12, md=12, lg=4, xl=4
        ),
        ], justify='start'),  # Horizontal:start,center,end,between,around
    dbc.Row([
        dbc.Col([
            html.P("Total Subsidy vs type of organization:",
                   style={"textDecoration": "underline"}),
            dcc.Checklist(id='my-checklist', value=['active', 'completed'],
                          options=[{'label':x, 'value':x}
                                  for x in sorted(df['ACTIVE'].unique())],
                          labelClassName="mr-3"),
            dcc.Graph(id='my-hist', figure={}),
        ], #width={'size':4, 'offset':0, 'order':1},
           xs=12, sm=12, md=12, lg=4, xl=4
        ),
        dbc.Col([
            html.P("Status application qua submission date:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-dpdn', multi=False, value='complete',
                         options=[{'label':x, 'value':x}
                                  for x in sorted(df['STATUS'].unique())], 
                                  
                        ),
            dcc.Graph(id='line-fig', figure={})
        ], #width={'size':4, 'offset':0, 'order':2},
           xs=12, sm=12, md=12, lg=4, xl=4
        ),
        
        dbc.Col([
            html.P("Number of applications vs Total Grant:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-dpdn2', multi=True, 
            value=['Type_1', 'Type_2'], options=[{'label':x, 'value':x}
                                  for x in sorted(df['ORG_TYPE'].unique())],
                                   ),
            dcc.Graph(id='line-fig2', figure={})
        ], #width={'size':4, 'offset':0, 'order':3},
          xs=12, sm=12, md=12, lg=4, xl=4
        ),
        
        ], align="center")  # Vertical: start, center, end
], fluid=True)

# Callback section: connecting the components
# ************************************************************************
# Pie chart
@app.callback(
    Output("pie-graph", "figure"), 
    Input("names", "value"))
def generate_chart(names):
    dff=df
    for value in dff['LABEL']:
        if value != value:
            #found NaN which gives null category in piechart
            print("found Nan")
    fig = px.pie(data_frame=dff, names=names, hole=.3)
    return fig

# Pie chart2
@app.callback(
    Output("pie-graph1", "figure"), 
    Input("names1", "value"))
def generate_chart(names1):
    dff=df
    fig1 = px.pie(data_frame=dff, names=names1, hole=.3)
    return fig1

# Histogram
@app.callback(
    Output('line-fig3', 'figure'),
    Input('my-dpdn3', 'value')
)
def update_graph(bonusorgtype):
    dff = df[df['ORG_TYPE'].isin(bonusorgtype)]
    dfff = dff.groupby(['ORG_NAME']).size().to_frame().sort_values([0], ascending = False).head(10).reset_index()
    figln3 = px.histogram(dfff,x=0,y='ORG_NAME').update_yaxes(type="category", categoryorder="total descending")
    figln3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_title=None, yaxis_title=None)
    return figln3

# Histogram
@app.callback(
    Output('my-hist', 'figure'),
    Input('my-checklist', 'value')
)
def update_graph(result_slctd):
    dff = df[df['ACTIVE'].isin(result_slctd)]
    fighist = px.histogram(dff, x='ORG_TYPE', labels={"PREVIOUSLY GRANT REQUESTED": "previously grant requested?"}, y='SUBSIDY_TOTAL', color="PREVIOUSLY GRANT REQUESTED")
    fighist.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_title=None, yaxis_title=None)
    return fighist


# Line chart - multiple
@app.callback(
    Output('line-fig2', 'figure'),
    Input('my-dpdn2', 'value')
)
def update_graph(bonusorgtype):
    dff = df[df['ORG_TYPE'].isin(bonusorgtype)]
    figln2 = px.histogram(dff, x="SUBSIDY_TOTAL")
    return figln2
# Line chart - Single
@app.callback(
    Output('line-fig', 'figure'),
    Input('my-dpdn', 'value')
)
def update_graph(status_slctd):
    dff = df[df['STATUS']==status_slctd]
    #figln = px.line(dff, x='Date', y='High')
    figln = px.histogram(dff, x='Inzenddatum', labels={"ACTIVE": "RESULT"}, color='ACTIVE')
    return figln
if __name__=='__main__':
    app.run_server(debug=True, port=8000)

    
# https://youtu.be/0mfIK8zxUds
