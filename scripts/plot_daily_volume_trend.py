import os
import matplotlib.pyplot as plt
from scripts.query_daily_volume import get_daily_trade_volume
import matplotlib.ticker as ticker

df = get_daily_trade_volume()
df["total_volume_mn"] = df["total_volume"] / 1e6  

plt.figure(figsize=(12, 6))
plt.plot(df["trade_date"], df["total_volume_mn"], marker="o", linestyle="-", color="purple")
plt.xlabel("Date")
plt.ylabel("Total Traded Volume (in Millions)")
plt.title("Daily Bulk Deal Volume Trend")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

os.makedirs("plots", exist_ok=True)
plt.savefig("plots/daily_volume_trend.png")
plt.show()
