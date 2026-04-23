import requests
from config import API_KEY

def fetch_weather(city):
    if not city:
        return None

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": f"{city},IN",      # use India country code
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        # if city invalid
        if response.status_code != 200 or "main" not in data:
            return None

        weather = {
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "description": data["weather"][0]["description"],
            "city": data["name"]
        }

        return weather

    except requests.exceptions.RequestException:
        return None