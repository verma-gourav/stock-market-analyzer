import os
import matplotlib.pyplot as plt
from scripts.query_buy_sell_distribution import get_buy_sell_distribution

df = get_buy_sell_distribution()

# color mapping
colors = ['green' if lbl == 'BUY' else 'red' for lbl in df['deal_type']]

# plot
plt.figure(figsize=(7,7))
plt.pie(df['total_volume'], labels=df['deal_type'], autopct='%1.1f%%', startangle=90, colors=colors)
plt.title("BUY vs SELL Volume Distribution (Bulk Deals)")
plt.axis('equal')

#save
os.makedirs("plots", exist_ok=True)
plt.savefig("plots/buy_sell_pie.png")
plt.show()