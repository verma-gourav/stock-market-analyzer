from db.utils import get_connection
import pandas as pd

def get_daily_trade_volume():
    conn = get_connection()
    query = """
    SELECT trade_date, SUM(quantity) AS total_volume
    FROM bulk_deals
    GROUP BY trade_date
    ORDER BY trade_date;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Parse dates
    df["trade_date"] = pd.to_datetime(df["trade_date"]) 
    return df
