import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import os
from modules.data_fetcher import get_crypto_prices, get_stock_prices



def update_market_data():
    
    btc, eth, sol, dog = get_crypto_prices()

    apple, tesla = get_stock_prices()

    # Create data dictionary
    data = {
    "time": [datetime.now()],
    "bitcoin": [btc],
    "ethereum": [eth],
    "solana": [sol],
    "dogecoin": [dog],
    "apple": [apple],
    "tesla": [tesla]
}

    df = pd.DataFrame(data)

    file_exists = os.path.isfile("data/market_data.csv")

    # Save data to CSV
    df.to_csv(
    "data/market_data.csv",
    mode="a",
    header=not os.path.exists("data/market_data.csv"),
    index=False
)

    print("Data Saved:", btc, eth, sol, dog ,apple , tesla)

    # Update chart
    create_interactive_chart()



def create_interactive_chart():

    df = pd.read_csv("data/market_data.csv")

    df["time"] = pd.to_datetime(df["time"], errors="coerce")

    # ---------------- CRYPTO CHART ----------------
    crypto_fig = go.Figure()

    crypto_fig.add_trace(go.Scatter(
        x=df["time"],
        y=df["bitcoin"],
        mode='lines',
        name="Bitcoin"
    ))

    crypto_fig.add_trace(go.Scatter(
        x=df["time"],
        y=df["ethereum"],
        mode='lines',
        name="Ethereum"
    ))

    crypto_fig.add_trace(go.Scatter(
        x=df["time"],
        y=df["solana"],
        mode='lines',
        name="Solana"
    ))

    crypto_fig.add_trace(go.Scatter(
        x=df["time"],
        y=df["dogecoin"],
        mode='lines',
        name="Dogecoin"
    ))

    crypto_fig.update_layout(
        title="Crypto Market Trends",
        xaxis_title="Time",
        yaxis_title="Price (USD)"
    )

    crypto_fig.write_html("static/crypto_chart.html")

    # ---------------- STOCK CHART ----------------
    stock_fig = go.Figure()

    stock_fig.add_trace(go.Scatter(
        x=df["time"],
        y=df["apple"],
        mode='lines',
        name="Apple"
    ))

    stock_fig.add_trace(go.Scatter(
        x=df["time"],
        y=df["tesla"],
        mode='lines',
        name="Tesla"
    ))

    stock_fig.update_layout(
        title="Stock Market Trends",
        xaxis_title="Time",
        yaxis_title="Price (USD)"
    )

    stock_fig.write_html("static/stock_chart.html")

    print("Charts Updated Successfully")


if __name__ == "__main__":
    update_market_data()    