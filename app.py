from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "JackFruit", "Oranges"],
    "Amount": [4, 1, 2, 2, 4, 2],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "SV"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(
        children='''
            Dash: A web application framework for your data.
        '''),

    dcc.Graph(
        id='example graph',
        figure=fig
    )
]
)

if __name__ == '__main__':
    app.run_server(debug=True)