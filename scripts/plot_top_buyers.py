import os
import matplotlib.pyplot as plt
from scripts.query_top_buyers import get_top_buyers

df = get_top_buyers(limit=10)

df['total_bought_billion'] = df['total_bought'] / 1e9

# plotting
plt.figure(figsize=(12,6))
plt.barh(df['client_name'], df['total_bought_billion'], color='steelblue')
plt.xlabel("Total Quantity Bought (in Billions)")
plt.title("Top 10 Buying Clients (Bulk Deals)")

plt.gca().invert_yaxis()

# save
os.makedirs("plots", exist_ok=True)
plt.tight_layout()
plt.savefig("plots/top_buyers.png")
plt.show()