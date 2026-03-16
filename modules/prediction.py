import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_bitcoin_trend():

    df = pd.read_csv("data/market_data.csv")

    # df = df[["time","bitcoin"]]
    df.columns = ["time","bitcoin","ethereum","solana","dogecoin","apple","tesla"]

    df["index"] = range(len(df))

    X = df[["index"]]
    y = df["bitcoin"]

    model = LinearRegression()
    model.fit(X,y)

    # next_index = pd.DataFrame({"index":[len(df)]})
    # predicted = model.predict(next_index)[0]
    predicted = model.predict([[len(df)]])[0]

    current = df["bitcoin"].iloc[-1]

    if predicted > current:
        trend = "UP"
    else:
        trend = "DOWN"

    return current, round(predicted,2), trend