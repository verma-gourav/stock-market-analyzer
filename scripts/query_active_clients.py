import pandas as pd
from db.utils import get_connection

def get_most_active_clients():
    conn = get_connection()
    query = """
    SELECT client_name, COUNT(*) AS deal_count, SUM(quantity) as total_qty
    FROM bulk_deals
    GROUP BY client_name
    ORDER BY deal_count DESC
    LIMIT 10
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df