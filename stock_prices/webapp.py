
import dash_bootstrap_components as dbc
import dash
from dash import Input, Output, State, html, dcc
import plotly.graph_objects as go
import plotly.express as px
import bigquery


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
# df = px.data.stocks()
df = bigquery.query_bq()
print(df.head())
server = app.server
app.config.suppress_callback_exceptions = True


def stock_prices():
    # Function for creating line chart showing Google stock prices over time 
    # fig = go.Figure([go.Scatter(x = df['Date'], y = df['Close'],
    #                  line = dict(color = 'Symbol', width = 4), name = 'Google')
    #                  ])
    fig = px.scatter(df, x = 'Date', y = 'Close', color= 'Symbol' )
    fig.update_layout(title = 'GOOG - Prices Over Time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig  

stock_price_graph = dcc.Graph(id = 'line_plot', figure = stock_prices())    
dropdown = dbc.Select( id = 'dropdown',
            options = [
                {'label':'Google', 'value':'GOOG' },
                {'label': 'Apple', 'value':'AAPL'},
                {'label': 'Amazon', 'value':'AMZN'},
                ],
            value = 'GOOG',     
            )

app.layout = html.Div(id = 'parent', children = [ 
    html.Div(
        [
            html.H1(id = 'H1', children = 'Stock prices over time', style = {'textAlign':'center','marginTop':40,'marginBottom':40}),
            dropdown,
            stock_price_graph     
        ]
    )
    ]
)

@app.callback(Output(component_id='line_plot', component_property= 'figure'),
              Output(component_id='H1', component_property='children'),
              Input(component_id='dropdown', component_property= 'value'))
def graph_update(dropdown_value):
    labels = {
        'GOOG':'Google',
        'AAPL':'Apple',
        'AMZN':'Amazon'
    }

    fig = px.scatter(df.loc[df['Symbol'] == dropdown_value], x = 'Date', y = 'Close', color= 'Symbol' )
    # go.Figure([go.Scatter(x = df['Date'], y = df['Symbol'] = df['{}'.format(dropdown_value)],\
    #                  line = dict(color = 'firebrick', width = 4))
    #                  ])
    
    fig.update_layout(title = '',
                      xaxis_title = 'Date',
                      yaxis_title = 'Close'
                      )
    return fig, f'{labels[dropdown_value]} Prices Over Time'



if __name__ == "__webapp__":
    app.run_server(debug=True, host="0.0.0.0", port=8080, use_reloader=False)