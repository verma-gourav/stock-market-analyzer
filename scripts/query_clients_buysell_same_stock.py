import pandas as pd
from db.utils import get_connection

def get_clients_buysell_same_stock_volumes():
    conn = get_connection()
    query = """
    SELECT symbol, client_name, deal_type, SUM(quantity) AS total_qty
    FROM bulk_deals
    GROUP BY symbol, client_name, deal_type
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df