# from fastapi import FastAPI
# import uvicorn
from fruitlib.ranfruit import fruit_generator
import dash_bootstrap_components as dbc
import dash
from dash import Input, Output, State, html, dcc

# app = FastAPI()
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
server = app.server
app.config.suppress_callback_exceptions = True

@app.get("/")
async def root():
    return {"message": "Hello Functions From Zero 2"}

@app.get("/fruits/{fruit}")
async def myfruit(fruit: str):
    """Adds a fruit to random fruit"""

    chosen_random_fruit = fruit_generator(fruit)
    return {"random_fruit": chosen_random_fruit}

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8080, use_reloader=False)