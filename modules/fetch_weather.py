import requests
from config import API_KEY, City

def fetch_weather(city):
    if not city:
        print("No city provided")
        return None

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        print("requested city:", city)  # Debugging line to check the requested city
        print("API response:", data)  # Debugging line to check the API response

        if "main" not in data:
            print("API Error:", data)
            return None

        weather = {
            "temperature": data["main"]["temp"],   
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
        }

        return weather

    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None