from flask import Flask, render_template, request
import os
import sys
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from modules.fetch_weather import fetch_weather
from modules.store_data import save_to_csv
from modules.predict import predict_temperature

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

DATA_FILE = os.path.join(BASE_DIR, "data", "weather_data.csv")

@app.route("/", methods=["GET", "POST"])
def home():
    try:
        if request.method == "POST":
            city = request.form.get("city")

            if not city:
                return render_template(
                    "index.html",
                    error="Enter city",
                    city=None,
                    dates=[],
                    temps=[],
                    humidities=[]
                )

            data = fetch_weather(city)

            if not data:
                return render_template(
                    "index.html",
                    error="City not found",
                    city=None,
                    dates=[],
                    temps=[],
                    humidities=[]
                )

            save_to_csv(data)

            prediction = None
            if os.path.exists(DATA_FILE):
                try:
                    prediction = predict_temperature()
                except Exception:
                    prediction = None

            dates = []
            temps = []
            humidities = []

            if os.path.exists(DATA_FILE):
                df = pd.read_csv(DATA_FILE)

                df["date"] = pd.to_datetime(df["date"], errors="coerce")
                df["temp"] = pd.to_numeric(df["temp"], errors="coerce")
                df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce")

                df = df.dropna()
                df = df.tail(10)

                dates = df["date"].dt.strftime("%d-%m %H:%M").tolist()
                temps = df["temp"].tolist()
                humidities = df["humidity"].tolist()

            return render_template(
                "index.html",
                city=city,
                temp=data["temperature"],
                humidity=data["humidity"],
                pressure=data["pressure"],
                description=data["description"],
                prediction=round(prediction, 2) if prediction is not None else None,
                dates=dates,
                temps=temps,
                humidities=humidities,
                error=None
            )

        return render_template(
            "index.html",
            dates=[],
            temps=[],
            humidities=[]
        )

    except Exception as e:
        return render_template(
            "index.html",
            error=str(e),
            dates=[],
            temps=[],
            humidities=[]
        )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)