import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf # type: ignore
from datetime import timedelta

symbol = "STLTECH" 
trade_date = "2025-06-16"  

start = pd.to_datetime(trade_date) - timedelta(days=3)
end = pd.to_datetime(trade_date) + timedelta(days=5)

df = yf.download(symbol + ".NS", start=start.strftime('%Y-%m-%d'), end=end.strftime('%Y-%m-%d'))

plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Close"], marker='o', linestyle='-', color="teal")
plt.axvline(pd.to_datetime(trade_date), color='red', linestyle='--', label="BUY Trade Date")
plt.title(f"Price Movement: {symbol} Around BUY on {trade_date}")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(f"plots/price_trend_{symbol}.png")
plt.show()
