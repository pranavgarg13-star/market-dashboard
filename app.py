from flask import Flask, render_template, send_file
from modules.prediction import predict_bitcoin_trend
import pandas as pd

app = Flask(__name__)

@app.route("/")
def dashboard():

    df = pd.read_csv("data/market_data.csv")

    df.columns = ["time","bitcoin","ethereum","solana","dogecoin","apple","tesla"]

    latest = df.iloc[-1]
    previous = df.iloc[-2]

    btc_change = (latest["bitcoin"] - previous["bitcoin"]) / previous["bitcoin"] * 100
    eth_change = (latest["ethereum"] - previous["ethereum"]) / previous["ethereum"] * 100
    sol_change = (latest["solana"] - previous["solana"]) / previous["solana"] * 100
    doge_change = (latest["dogecoin"] - previous["dogecoin"]) / previous["dogecoin"] * 100

    current, predicted, trend = predict_bitcoin_trend()

    return render_template(
        "dashboard.html",

        btc=latest["bitcoin"],
        eth=latest["ethereum"],
        sol=latest["solana"],
        doge=latest["dogecoin"],
        aapl=latest["apple"],
        tsla=latest["tesla"],

        btc_change=round(btc_change,2),
        eth_change=round(eth_change,2),
        sol_change=round(sol_change,2),
        doge_change=round(doge_change,2),

        predicted=predicted,
        trend=trend
    )

@app.route("/crypto_chart.html")
def crypto_chart():
    return send_file("static/crypto_chart.html")

@app.route("/stock_chart.html")
def stock_chart():
    return send_file("static/stock_chart.html")

if __name__ == "__main__":
    app.run(debug=True)