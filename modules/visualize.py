import pandas as pd
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import os

def plot_temperature():
    file_path = "data/weather_data.csv"

    if not os.path.exists(file_path):
        return

    df = pd.read_csv(file_path)

    df = df[df["date"] != "date"]


    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["temp"] = pd.to_numeric(df["temp"], errors="coerce")


    df = df.dropna(subset=["date", "temp"])

    if df.empty:
        return

    os.makedirs("static", exist_ok=True)

    plt.figure(figsize=(10,5))
    plt.plot(df["date"], df["temp"], marker="o", linewidth=2)

    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trend")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("static/temp_plot.png")
    plt.close()