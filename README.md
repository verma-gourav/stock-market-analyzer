# 📈 Indian Stock Market Analyzer & Suspicious Trade Detector

A complete data analytics and anomaly detection tool designed to analyze bulk deal activities in the Indian equity market. Integrates real market data, generates insightful visualizations, flags potentially suspicious trades, and includes an interactive CLI and notebook-based exploration.

---

## 📅 Project Overview

This project helps investors, analysts, and regulators:

- Understand **who** is trading in bulk
- Visualize **market trends**
- Detect **potential insider trading** or **price manipulation**

---

## 📁 Dataset Description

### 1. Bulk Deal Dataset (`bulk_deals.csv`)

- Source: \[NSE Bulk Deals Data]
- Contains:

  - `symbol` (Stock Symbol)
  - `client_name`
  - `deal_type` (BUY or SELL)
  - `quantity`
  - `trade_date`
  - `price` (trade price)

### 2. Price Data (`price_data.csv`)

- Source: \[Yahoo Finance via `yfinance`]
- Collected using a 2-day window around trade dates
- Contains:

  - `symbol`
  - `trade_date`
  - `close_price` (closing price of trade day)

### 3. Merged Dataset (`bulk_deals_with_price.csv`)

- Added calculated:

  - `total_trade_value = quantity x close_price`

### 4. Anomalies Dataset (`anomalies_price_jump.csv`)

- Contains:

  - Trades where price increased >5% the next day
  - Fields: `symbol`, `client_name`, `price_trade_day`, `price_next_day`, `pct_change`, `flagged`

---

## 🎯 Features

### ✅ Visual Reports:

### Top 10 Clients by Quantity Bought

![](plots\top_buyers.png)

### Most Traded Stocks

![](plots\top_traded_stocks.png)

### Deal Type Split (BUY vs SELL)

![](plots\buy_sell_pie.png)

### Daily Volume Trend

![](plots\daily_volume_trend.png)

### Clients Buying & Selling Same Stock (Heatmap)

![](plots\clients_buysell_heatmap.png)

### Anomaly Heatmap

![](plots\anomaly_heatmap.png)

### Top Anomalous Trades by Value

![](plots\top_anomalous_buys.png)

### 📊 Price-Based Anomaly Detection

- Flags any BUY deal where price jumps >5% next day
- Uses Yahoo Finance historical data

### 🔹 CLI Tool (Command Line Interface)

- Interactive filtering and export tool
- Options:

  - View all anomalies
  - Filter by symbol, date, or client
  - Export flagged results

---

## 📆 Workflow Summary

```bash
# 1. Fetch price data
python -m scripts.fetch_prices_yf

# 2. Merge datasets and calculate value
python -m scripts.merge_bulk_price

# 3. Detect anomalies
python -m scripts.detect_price_jump

# 4. Visualize insights
python -m scripts.plot_top_buyers

# 5. Use CLI tool
python -m cli
```

---

## 🎓 Jupyter Notebook

- Explore insights and generate visual reports interactively
- Notebook: `notebooks/StockAnalyzer_Insights.ipynb`
- Includes:

  - Summary statistics
  - Chart rendering
  - Inline anomaly explanation

---

## 🔧 Tech Stack

- Python 3.x
- Pandas, Matplotlib, Seaborn
- SQLite3 for data storage
- yfinance for stock prices
- CLI via argparse
- Jupyter Notebook for documentation

---

## 🌟 Key Insights

> "Multiple clients bought _APOLLO_ stock on May 27. The stock surged **13.8%** next day."

> "Client `GRAVITON RESEARCH CAPITAL LLP` repeatedly appears in trades flagged as suspicious."

> "Stocks like _KBCGLOBAL_ and _ALUWIND_ saw **>7% price jumps** right after large BUYs."

---

## 🌐 Project Structure

```
Stock-Market-Analyzer/
├── db/
│   └── market_data.db
├── data/
│   ├── bulk_deals.csv
│   ├── price_data.csv
│   └── anomalies_price_jump.csv
├── plots/
│   └── [All .png plots]
├── scripts/
│   ├── fetch_prices_yf.py
│   ├── detect_price_jump.py
│   ├── merge_bulk_price.py
│   └── plot_*.py
├── notebooks/
│   └── StockAnalyzer_Insights.ipynb
│── cli.py
└── README.md
```

---

## 💼 License

MIT License

---

## 🏆 Credits

Built by \[Gourav Verma] ✨ | Data from NSE & Yahoo Finance | Powered by Python

---

## 🏷️ Tags

`data-science` · `stock-market` · `finance` · `india` · `nse` · `bulk-deals` · `anomaly-detection` · `pandas` · `matplotlib` · `cli-tool` · `jupyter-notebook`
