import os
import matplotlib.pyplot as plt
from scripts.query_top_stocks import get_top_stocks
import matplotlib.ticker as ticker

df = get_top_stocks(limit=10)

df['total_volume_milli'] = df['total_volume'] / 1e6

# plotting
plt.figure(figsize=(12,6))
plt.barh(df['symbol'], df['total_volume_milli'], color='darkorange')
plt.xlabel("Total Volume Traded (in Millions)")
plt.title("Top 10 Traded Stocks by Volume (Bulk Deals)")

plt.gca().invert_yaxis()
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))

# save
os.makedirs("plots", exist_ok=True)
plt.tight_layout()
plt.savefig("plots/top_traded_stocks.png")
plt.show()