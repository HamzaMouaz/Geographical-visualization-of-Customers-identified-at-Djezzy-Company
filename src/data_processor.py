import pandas as pd
from src.config import DATA_PATH, COL_DATE

def load_data():
    """Charge le fichier Excel principal."""
    return pd.read_excel(DATA_PATH)

def clean_data(df):
    """Nettoie les dates et ajoute la colonne année."""
    df[COL_DATE] = pd.to_datetime(df[COL_DATE], errors='coerce')
    df.dropna(subset=[COL_DATE], inplace=True)
    df['Annee_Identification'] = df[COL_DATE].dt.year
    return df

def get_revenue_by_region(df):
    """Calcule le revenu total par région."""
    return df.groupby('BU')['REVENUE_LAST_12_MONTHS'].sum().reset_index(name='Revenue par region')

def get_clients_by_year(df):
    """Compte le nombre de clients par année d'identification."""
    return df.groupby('Annee_Identification')['CUST_ID'].count().reset_index()