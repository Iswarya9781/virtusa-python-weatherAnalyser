from flask import Flask, render_template,request
import os
import sys

# Base directory setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# Correct imports
from modules.fetch_weather import fetch_weather
from modules.store_data import save_to_csv
from modules.analyze import analyze_data
from modules.visualize import plot_temperature
from modules.predict import predict_temperature

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

@app.route("/", methods=["GET", "POST"])
def home():
    try:
        city = None

        # Get user input
        if request.method == "POST":
            city = request.form.get("city")
        if not city:
            return render_template(
                "index.html",
                 avg_temp=None,
                 avg_humidity=None,
                 prediction=None,
                 city=None,
                 error="Please enter a city"
    )

        print("Fetching data for:", city)

        data = fetch_weather(city)
        # Debugging line to check the fetched data
        if not data:
            raise RuntimeError("Invalid city or API error")

        save_to_csv(data)

        insights = analyze_data()
        plot_temperature()
        prediction = predict_temperature()

        return render_template(
            "index.html",
            avg_temp=round(insights["avg_temp"], 2),
            avg_humidity=round(insights["avg_humidity"], 2),
            prediction=round(prediction, 2),
            city=city,
            error=None
        )

    except Exception as e:
        return render_template(
            "index.html",
            avg_temp=None,
            avg_humidity=None,
            prediction=None,
            city=None,
            error=str(e)
        )

if __name__ == "__main__":
    app.run(debug=True)