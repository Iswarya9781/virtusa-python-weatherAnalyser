import os
import csv
from datetime import datetime

FILE_PATH = "data/weather_data.csv"

def save_to_csv(weather):
    os.makedirs("data", exist_ok=True)  # ✅ create folder if not exists

    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)

        
        if not file_exists:
            writer.writerow(["date", "temp", "humidity", "pressure"])

        writer.writerow([
            datetime.now(),
            weather["temperature"],
            weather["humidity"],
            weather["pressure"]
        ])