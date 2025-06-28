import pandas as pd
import yfinance as yf # type: ignore
from db.utils import get_connection
from datetime import timedelta

def fetch_close_prices(symbol_dates):
    results = []
    for symbol, date in symbol_dates:
        symbol_yf = symbol + ".NS"
        try:
            # getting 2 day window around trade
            df = yf.download(symbol_yf, start=date, end=(pd.to_datetime(date) + timedelta(days=2)).strftime('%Y-%m-%d'))
            if not df.empty and "Close" in df.columns:
                close_price = df["Close"].values[0].item()
                results.append((symbol, date, round(close_price, 2)))
        except Exception as e:
            print(f"Error fetching {symbol} on {date}: {e}")
            continue
    return pd.DataFrame(results, columns=["symbol", "trade_date", "close_price"])            

# loading distinct symbol+date pairs from db
conn = get_connection()
bulk_df = pd.read_sql_query("""
SELECT DISTINCT symbol, trade_date
FROM bulk_deals                           
""", conn)
conn.close()

bulk_df["trade_date"] = pd.to_datetime(bulk_df["trade_date"])

# fetching price data from yfinance
price_df = fetch_close_prices(bulk_df.itertuples(index=False, name=None))

# saving
price_df.to_csv("data/price_data.csv", index=False)
print("Saved fetched price data to data/price_data.csv")