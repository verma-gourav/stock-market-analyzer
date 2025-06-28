import argparse
import pandas as pd

def load_data():
    df = pd.read_csv("data/anomalies_price_jump.csv")
    return df

def filter_data(df, stock=None, client=None, date=None, flagged_only=False):
    if stock:
        df = df[df["symbol"].str.upper() == stock.upper()]
    if client:
        df = df[df["client_name"].str.contains(client, case=False)]
    if date:
        df = df[df["trade_date"] == date]
    if flagged_only:
        df = df[df["flagged"] == True]
    return df

def main():
    parser = argparse.ArgumentParser(description="Stock Market Anomaly Analyzer CLI")
    parser.add_argument("--stock", help="Filter by stock symbol")
    parser.add_argument("--client", help="Filter by client name (partial allowed)")
    parser.add_argument("--date", help="Filter by trade date (YYYY-MM-DD)")
    parser.add_argument("--export", help="Export filtered results to CSV")
    parser.add_argument("--flagged-only", action="store_true", help="Show only suspicious (flagged) trades")

    args = parser.parse_args()
    df = load_data()
    filtered = filter_data(df, args.stock, args.client, args.date, args.flagged_only)

    if filtered.empty:
        print("No matching records found.")
    else:
        print(filtered[["symbol", "client_name", "trade_date", "pct_change", "flagged"]])
        if args.export:
            filtered.to_csv(args.export, index=False)
            print(f"Exported to {args.export}")

if __name__ == "__main__":
    main()
