import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/anomalies_price_jump.csv")

df = df.drop_duplicates()

# sorting and taking top anomalies
df_top = df.sort_values("pct_change", ascending=False).head(10)

# plot
plt.figure(figsize=(12, 6))
plt.barh(df_top["client_name"] + " | " + df_top["symbol"], df_top["pct_change"], color="crimson")
plt.xlabel("Next Day Price Change (%)")
plt.title("Top 10 Anomalous Bulk BUY Trades by Price Jump")
plt.gca().invert_yaxis()
plt.tight_layout()

# save
plt.savefig("plots/top_anomalous_buys.png")
plt.show()