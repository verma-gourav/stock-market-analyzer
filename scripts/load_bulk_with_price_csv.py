import pandas as pd
import os
from db.utils import get_connection

csv_path = os.path.join("data", "bulk_deals_with_price.csv")
df = pd.read_csv(csv_path)

conn = get_connection()
df.to_sql("bulk_deals_with_price", conn, if_exists="replace", index=False)
conn.close()

print(f"Inserted {len(df)} records into 'bulk_deals_with_price' table.")
