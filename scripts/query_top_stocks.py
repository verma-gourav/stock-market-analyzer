import pandas as pd
from db.utils import get_connection

def get_top_stocks(limit=10):
    # db connection
    conn = get_connection()
    # query
    query = """
    SELECT symbol, SUM(quantity) AS total_volume
    FROM bulk_deals
    GROUP BY symbol
    ORDER BY total_volume DESC
    LIMIT 10
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df