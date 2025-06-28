import pandas as pd
import matplotlib.pyplot as plt
from db.utils import get_connection

conn = get_connection()
query = """
SELECT symbol, SUM(total_trade_value) AS total_value
FROM bulk_deals_with_price
GROUP BY symbol
ORDER BY total_value DESC
LIMIT 10;
"""
df = pd.read_sql_query(query, conn)
conn.close()

plt.figure(figsize=(12, 6))
plt.bar(df["symbol"], df["total_value"], color="cornflowerblue")
plt.ylabel("Total Trade Value (₹)")
plt.title("Top 10 Stocks by Total Trade Value")
plt.tight_layout()
plt.savefig("plots/top_stocks_by_value.png")
plt.show()
