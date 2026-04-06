import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "weather_data.csv"))

def analyze_data():
    # ✅ Check if file exists
    if not os.path.exists(DATA_FILE):
        return {"avg_temp": 0, "avg_humidity": 0}

    df = pd.read_csv(DATA_FILE)

    # ✅ Check if empty
    if df.empty:
        return {"avg_temp": 0, "avg_humidity": 0}
    df["temp"] = pd.to_numeric(df["temp"], errors="coerce")
    df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce")


    insights = {
        "avg_temp": df["temp"].mean(),          # ✅ correct column
        "avg_humidity": df["humidity"].mean()  # ✅ lowercase
    }

    return insights