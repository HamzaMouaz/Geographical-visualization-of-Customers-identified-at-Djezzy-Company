import os

# Chemins
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'POS_IDENTIFCIATION_CAMPAGNE_STAT.xlsx')

# Constantes de colonnes
COL_REVENUE = 'REVENUE_LAST_12_MONTHS'
COL_REGION = 'BU'
COL_DATE = 'DOC_VAL_DT'
COL_CUST_ID = 'CUST_ID'