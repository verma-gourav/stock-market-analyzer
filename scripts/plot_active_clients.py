import os
import matplotlib.pyplot as plt
from scripts.query_active_clients import get_most_active_clients

df = get_most_active_clients()

plt.figure(figsize=(12, 6))
plt.barh(df["client_name"], df["deal_count"], color="darkcyan")
plt.xlabel("Number of Deals")
plt.title("Top 10 Most Active Clients by Deal Count")
plt.gca().invert_yaxis()

os.makedirs("plots", exist_ok=True)
plt.tight_layout()
plt.savefig("plots/top_active_clients.png")
plt.show()
