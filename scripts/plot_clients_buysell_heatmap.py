import os
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore
from scripts.query_clients_buysell_same_stock import get_clients_buysell_same_stock_volumes

df = get_clients_buysell_same_stock_volumes()

# pivot to get BUY and SELL side by side
pivot = df.pivot_table(index=['client_name', 'symbol'], columns="deal_type", values="total_qty", fill_value=0)

# filtering those who did both
pivot = pivot[(pivot['BUY'] > 0) & (pivot['SELL'] > 0)]

# total volume traded
pivot["total_volume"] = pivot['BUY'] + pivot['SELL']

# pivot to heatmap format: client_name × symbol
heatmap_data = pivot.reset_index().pivot(index="client_name", columns="symbol", values="total_volume").fillna(0)

# top 20 clients and symbols
top_clients = heatmap_data.sum(axis=1).nlargest(20).index
top_symbols = heatmap_data.sum(axis=0).nlargest(20).index
heatmap_data = heatmap_data.loc[top_clients, top_symbols]

# plotting heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(heatmap_data, cmap="YlOrBr", linewidths=0.5, linecolor="gray")
plt.title("Clients Buying & Selling the Same Stock (Heatmap)")
plt.xlabel("Stock Symbol")
plt.ylabel("Client Name")
plt.tight_layout()
plt.savefig("plots/clients_buysell_heatmap.png")
plt.show()