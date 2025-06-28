import pandas as pd
import matplotlib.pyplot as plt
from db.utils import get_connection

conn = get_connection()
query = """
SELECT deal_type, SUM(total_trade_value) AS total_value
FROM bulk_deals_with_price
GROUP BY deal_type;
"""
df = pd.read_sql_query(query, conn)
conn.close()

colors = ["limegreen" if lbl == 'BUY' else "tomato" for lbl in df['deal_type']]

plt.figure(figsize=(6, 6))
plt.pie(df["total_value"], labels=df["deal_type"], autopct="%1.1f%%", startangle=140, colors=colors)
plt.title("Total Trade Value Distribution: BUY vs SELL")
plt.tight_layout()
plt.savefig("plots/value_pie.png")
plt.show()
