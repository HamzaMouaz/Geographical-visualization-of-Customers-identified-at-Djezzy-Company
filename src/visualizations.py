import plotly.express as px

def create_revenue_bar_chart(revenue_df):
    fig = px.bar(
        data_frame=revenue_df, 
        x='Revenue par region', 
        y='BU', 
        color='BU', 
        orientation='h', 
        title='Total des revenus par région'
    )
    return fig

def create_clients_year_chart(clients_df):
    fig = px.bar(
        data_frame=clients_df,
        x='Annee_Identification',
        y='CUST_ID',
        labels={'Annee_Identification': 'Année', 'CUST_ID': 'Nombre de clients'},
        title='Nombre de clients identifiés par année'
    )
    fig.update_xaxes(type='category')
    return fig