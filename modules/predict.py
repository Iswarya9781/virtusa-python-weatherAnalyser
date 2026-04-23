import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def predict_temperature():
    df = pd.read_csv("data/weather_data.csv")

    df["date"] = pd.to_datetime(df["date"])
    df["temp"] = pd.to_numeric(df["temp"])

    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year

    X = df[["day", "month", "year"]]
    y = df["temp"]

    model = RandomForestRegressor()
    model.fit(X, y)

    last = df.iloc[-1]

    future = pd.DataFrame([{
        "day": last["day"] + 1,
        "month": last["month"],
        "year": last["year"]
    }])

    pred = model.predict(future)

    return pred[0]