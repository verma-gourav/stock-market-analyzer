import pandas as pd
from db.utils import get_connection

def get_top_buyers(limit=10):
    # db connection
    conn = get_connection()
    
    # query
    query = """
    SELECT client_name, SUM(quantity) as total_bought
    from bulk_deals
    WHERE deal_type = "BUY"
    GROUP BY client_name
    ORDER BY total_bought DESC
    LIMIT 10
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df