import pandas as pd
import yfinance as yf # type: ignore
from datetime import timedelta

df = pd.read_csv("data/bulk_deals_with_price.csv", parse_dates=['trade_date'])

buy_df = df[df["deal_type"] == "BUY"].copy()

results = []

for _, row in buy_df.iterrows():
    symbol = row["symbol"]
    trade_date = row["trade_date"]
    price_on_trade_day = row["close_price"]
    symbol_yf = symbol + ".NS"

    try:
        next_day = trade_date + timedelta(days=1)
        df_next = yf.download(symbol_yf, start=next_day.strftime('%Y-%m-%d'), end=(next_day + timedelta(days=1)).strftime('%Y-%m-%d'))

        if not df_next.empty and "Close" in df_next.columns:
            price_next_day = df_next["Close"].values[0].item()
            pct_change = ((price_next_day - price_on_trade_day) / price_on_trade_day) * 100
            is_suspicious = pct_change > 5

            results.append({
                "symbol": symbol,
                "client_name": row["client_name"],
                "trade_date": trade_date,
                "price_trade_day": price_on_trade_day,
                "price_next_day": price_next_day,
                "pct_change": pct_change,
                "flagged": is_suspicious
            })
    except Exception as e:
        print(f"Error for {symbol} on {trade_date}: {e}")
        continue

# save and review
anomaly_df = pd.DataFrame(results)
anomaly_df.to_csv("data/anomalies_price_jump.csv", index=False)
print("Saved flagged anomalies to data/anomalies_price_jump.csv")