import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_temperature():
    df = pd.read_csv("data/weather_data.csv")
    print(df.head())
    print("CSV DATA:")
    df = df[df["date"] != "date"]
    df["date"] = pd.to_datetime(df["date"],errors="coerce")

    # Ensure static folder exists
    os.makedirs("static", exist_ok=True)

    plt.figure()
    plt.plot(df["date"], df["temp"])
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trend")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("static/temp_plot.png") 
    plt.close()
    print("✅ Graph saved successfully")