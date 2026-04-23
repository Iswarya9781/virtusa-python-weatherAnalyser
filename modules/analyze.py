import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "weather_data.csv"))

def analyze_data():
    if not os.path.exists(DATA_FILE):
        return {"avg_temp": 0, "avg_humidity": 0}

    df = pd.read_csv(DATA_FILE)

   
    df = df[df["date"] != "date"]
    df["temp"] = pd.to_numeric(df["temp"], errors="coerce")
    df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    df = df.dropna()

    if df.empty:
        return {"avg_temp": 0, "avg_humidity": 0}

    insights = {
        "avg_temp": df["temp"].mean(),
        "avg_humidity": df["humidity"].mean()
    }

    return insights