import dash
from dash import dcc, html
from src.data_processor import load_data, clean_data, get_revenue_by_region, get_clients_by_year
from src.visualizations import create_revenue_bar_chart, create_clients_year_chart

# Initialisation des données
df = load_data()
df = clean_data(df)

# Création de l'application Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard d'Identification Client"),
    
    html.Div([
        dcc.Graph(figure=create_revenue_bar_chart(get_revenue_by_region(df)))
    ]),
    
    html.Div([
        dcc.Graph(figure=create_clients_year_chart(get_clients_by_year(df)))
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)