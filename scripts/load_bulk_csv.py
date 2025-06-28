import pandas as pd
import sqlite3
import os

# file paths
csv_path = os.path.join("data", "nse_bulk_deals.csv")
db_path = os.path.join("db", "market_data.db")

# loading csv
df = pd.read_csv(csv_path)

# normalizing column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

'''print("📋 Columns in CSV:", df.columns.tolist())
print(df.head())'''

# renaming columns
df = df.rename(columns={
    'date': 'trade_date',
    'symbol': 'symbol',
    'security_name': 'security_name',
    'client_name': 'client_name',
    'buy_/_sell': 'deal_type',
    'quantity_traded': 'quantity',
    'trade_price_/_wght._avg._price': 'trade_price'
})

# cleaning data
df["trade_date"] = pd.to_datetime(df['trade_date'], format="%d-%b-%Y", errors="coerce")
df["quantity"] = df['quantity'].astype(str).str.replace(",", "").astype(float)
df["trade_price"] = df['trade_price'].astype(str).str.replace(",", "").astype(float)
df["deal_type"] = df['deal_type'].str.upper().str.strip()

# dropping extra column 'remarks'
df = df[['symbol', 'security_name', 'client_name', 'deal_type', 'quantity', 'trade_price', 'trade_date']]

# connecting to sqlite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# creating table
cursor.execute("""
CREATE TABLE IF NOT EXISTS bulk_deals(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT,
    security_name TEXT,
    client_name TEXT,
    deal_type TEXT,
    quantity INTEGER,
    trade_price REAL,
    trade_date DATE
)
""")

#inserting into db
df.to_sql("bulk_deals", conn, if_exists='append', index=False)
print(f"✅ {len(df)} records inserted into 'bulk_deals' table.")

conn.close()
