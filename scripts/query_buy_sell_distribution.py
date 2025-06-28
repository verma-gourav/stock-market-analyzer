import pandas as pd
from db.utils import get_connection

def get_buy_sell_distribution():
    conn = get_connection()
    query = """
    SELECT deal_type, SUM(quantity) AS total_volume
    FROM bulk_deals
    GROUP BY deal_type
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df