import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

# Load and filter
df = pd.read_csv("data/anomalies_price_jump.csv")
df = df[df["flagged"] == True]

# Count suspicious trades
pivot_df = df.pivot_table(index="client_name", columns="symbol", values="flagged", aggfunc="sum", fill_value=0)

# Get top 10 clients & top 10 stocks
top_clients = pivot_df.sum(axis=1).sort_values(ascending=False).head(10).index
top_stocks = pivot_df.sum(axis=0).sort_values(ascending=False).head(10).index
pivot_top = pivot_df.loc[top_clients, top_stocks]

# Plot
plt.figure(figsize=(14, 8))
sns.heatmap(pivot_top, annot=True, fmt="d", cmap="Reds", linewidths=0.5, linecolor='gray')
plt.title("Top Clients vs Stocks – Suspicious BUY Frequency")
plt.xlabel("Stock Symbol")
plt.ylabel("Client Name")
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig("plots/anomaly_heatmap.png")
plt.show()
