import os
import pandas as pd
from db.utils import get_connection

conn = get_connection()
bulk_df = pd.read_sql_query("SELECT * FROM bulk_deals", conn)
conn.close()

# cleaning quantity
bulk_df["quantity"] = bulk_df["quantity"].astype(str).str.replace(",", "").astype(int)
bulk_df["trade_date"] = pd.to_datetime(bulk_df["trade_date"])

# loading close price data
price_df = pd.read_csv("data/price_data.csv")
price_df["trade_date"] = pd.to_datetime(price_df["trade_date"])

# merging both on 'symbol' and 'trade_date'
merged_df = pd.merge(bulk_df, price_df, on=['symbol', 'trade_date'], how="inner")

# total trade value
merged_df["total_trade_value"] = merged_df["quantity"] * merged_df["close_price"]

# saving data
merged_df.to_csv("data/bulk_deals_with_price.csv", index=False)
print("Merged data saved to 'data/bulk_deals_with_price.csv'")