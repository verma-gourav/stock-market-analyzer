import pandas as pd
from db.utils import get_connection

def show_menu():
    print("\n STOCK MARKET ANALYZER MENU")
    print("1. Top Buying Clients")
    print("2. Top Traded Stocks by Quantity")
    print("3. Show All Flagged Anomalies")
    print("4. Show Anomalies for Specific Stock")
    print("5. Exit")

def top_buying_clients():
    conn = get_connection()
    query = """
    SELECT client_name, SUM(quantity) AS total_bought
    FROM bulk_deals
    WHERE deal_type = 'BUY'
    GROUP BY client_name
    ORDER BY total_bought DESC
    LIMIT 10;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    print("\n Top 10 Buying Clients:")
    print(df.to_string(index=False))

def top_traded_stocks():
    conn = get_connection()
    query = """
    SELECT symbol, SUM(quantity) AS total_quantity
    FROM bulk_deals
    GROUP BY symbol
    ORDER BY total_quantity DESC
    LIMIT 10;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    print("\n Top 10 Traded Stocks:")
    print(df.to_string(index=False))

def show_all_anomalies():
    df = pd.read_csv("data/anomalies_price_jump.csv")
    df_flagged = df[df["flagged"] == True]
    print("\n Flagged Anomalies (Price Jump > 5%):")
    print(df_flagged[["symbol", "client_name", "trade_date", "pct_change"]].to_string(index=False))

def anomalies_for_stock():
    stock = input("Enter stock symbol (e.g., APOLLO): ").strip().upper()
    df = pd.read_csv("data/anomalies_price_jump.csv")
    df_flagged = df[(df["flagged"] == True) & (df["symbol"] == stock)]
    if df_flagged.empty:
        print(f" No anomalies found for {stock}")
    else:
        print(f"\n Anomalies for {stock}:")
        print(df_flagged[["client_name", "trade_date", "pct_change"]].to_string(index=False))

def main():
    while True:
        show_menu()
        choice = input("\nEnter choice (1-5): ").strip()

        if choice == '1':
            top_buying_clients()
        elif choice == '2':
            top_traded_stocks()
        elif choice == '3':
            show_all_anomalies()
        elif choice == '4':
            anomalies_for_stock()
        elif choice == '5':
            print(" Exiting. Thank you!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
