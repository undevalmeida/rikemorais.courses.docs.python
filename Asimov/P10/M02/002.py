import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Layout
app.layout = html.Div(id="div1",
                      children=[
                          html.H1("Hello, Dash!", id="h1", style={"color": "red"}),
                          html.Div(
                              "Dash: Um framework para criar interfaces web para Python.", id="div2")
                      ]
                      )

if __name__ == "__main__":
    app.run_server(debug=True)
