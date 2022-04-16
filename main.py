
import dash_bootstrap_components as dbc
import dash
from dash import Input, Output, State, html, dcc
import plotly.graph_objects as go
import plotly.express as px


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
df = px.data.stocks()
server = app.server
app.config.suppress_callback_exceptions = True


def stock_prices():
    # Function for creating line chart showing Google stock prices over time 
    fig = go.Figure([go.Scatter(x = df['date'], y = df['GOOG'],\
                     line = dict(color = 'firebrick', width = 4), name = 'Google')
                     ])
    fig.update_layout(title = 'Prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig  

 
app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Styling using html components', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        
        dcc.Graph(id = 'line_plot', figure = stock_prices())    
    ]
                     )


dcc.Dropdown( id = 'dropdown',
options = [
    {'label':'Google', 'value':'GOOG' },
    {'label': 'Apple', 'value':'AAPL'},
    {'label': 'Amazon', 'value':'AMZN'},
    ],
value = 'GOOGL'       
)

@app.callback(Output(component_id='line_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    fig = go.Figure([go.Scatter(x = df['date'], y = df['{}'.format(dropdown_value)],\
                     line = dict(color = 'firebrick', width = 4))
                     ])
    
    fig.update_layout(title = 'Stock prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig 



# # @app.get("/")
# def root():
#     return {"message": "Hello Functions From Zero 2"}

# # @app.get("/fruits/{fruit}")
# def myfruit(fruit: str):
#     """Adds a fruit to random fruit"""

#     chosen_random_fruit = fruit_generator(fruit)
#     return {"random_fruit": chosen_random_fruit}

# app.layout = html.Div(
#     [
#         dbc.Row(html.A(), style={"height": "20px"}),
#         dbc.Row(
#             dbc.Col([html.H1("434 project")]),
#             justify="center",
#             align="center",
#             style={"text-align": "center"},
#         ),
#     ],
# )

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8080, use_reloader=False)