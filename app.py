from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div(
    style={
        'backgroundColor': '#f8fafc',
        'minHeight': '100vh',
        'padding': '30px',
        'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif'
    },
    children=[
        # Title (H1)
        html.H1(
            children='My first dash',
            style={
                'textAlign': 'center',
                'color': '#1e293b',
                'border': '2px solid #ef4444',
                'borderRadius': '8px',
                'width': '300px',
                'margin': '0 auto 25px auto',
                'padding': '8px 0',
                'backgroundColor': '#ffffff',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.05)'
            }
        ),

        # Dropdown Container
        html.Div(
            style={'width': '250px', 'margin': '0 auto 20px auto'},
            children=[
                dcc.Dropdown(
                    df.country.unique(),
                    'Canada',
                    id='dropdown-selection',
                    clearable=False
                )
            ]
        ),

        # Graph Container
        html.Div(
            style={
                'backgroundColor': '#ffffff',
                'borderRadius': '12px',
                'padding': '15px',
                'boxShadow': '0 4px 6px -1px rgba(0, 0, 0, 0.05)',
                'border': '1px solid #e2e8f0',
                'maxWidth': '900px',
                'margin': '0 auto'
            },
            children=[
                dcc.Graph(id='graph-content')
            ]
        )
    ]
)

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(valeur):
    dff = df[df.country == valeur]
    fig = px.line(
        dff, 
        x='year', 
        y='lifeExp',
        title=f'Life Expectancy in {valeur}',
        template='plotly_white'
    )
    fig.update_traces(line_color='#2563eb', line_width=2.5)
    return fig

if __name__ == '__main__':
    app.run(debug=True)