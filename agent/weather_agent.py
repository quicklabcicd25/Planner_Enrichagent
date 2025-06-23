import requests
import os
from dotenv import load_dotenv
load_dotenv()

class WeatherAgent:
    def get_weather(self, location):
        lat = location["latitude"]
        lon = location["longitude"]
        key = os.getenv("OPENWEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric"
        response = requests.get(url)
        data = response.json()
        return {
            "main": data.get("weather")[0]["main"],
            "description": data.get("weather")[0]["description"],
            "temp": data.get("main")["temp"]
        }
