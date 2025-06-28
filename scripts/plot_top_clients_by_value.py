import os
import pandas as pd
import matplotlib.pyplot as plt
from db.utils import get_connection

conn = get_connection()
query = """
SELECT client_name, SUM(total_trade_value) AS total_value
FROM bulk_deals_with_price
GROUP BY client_name
ORDER BY total_value DESC
LIMIT 10;
"""
df = pd.read_sql_query(query, conn)
conn.close()

plt.figure(figsize=(12, 6))
plt.barh(df["client_name"], df["total_value"], color="mediumseagreen")
plt.xlabel("Total Trade Value (₹)")
plt.title("Top 10 Clients by Total Trade Value")
plt.gca().invert_yaxis()
plt.tight_layout()

os.makedirs("plots", exist_ok=True)
plt.savefig("plots/top_clients_by_value.png")
plt.show()
