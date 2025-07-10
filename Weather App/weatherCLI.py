import argparse
from dotenv import load_dotenv
import requests
import os

load_dotenv()

parser = argparse.ArgumentParser(description = "Enter city name")
parser.add_argument("city", help="Enter city name to get the temperature")
args = parser.parse_args()

API_KEY = os.getenv("API_KEY")
url = f"http://api.openweathermap.org/data/2.5/weather?q={args.city}&appid={API_KEY}&units=metric"
try:
    response = requests.get(url, timeout=10 )
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

if data.get("main"):
    print(f"Weather in {args.city}: {data['main']['temp']} Degree C, Humidity: {data['main']['humidity']}, Description: {data['weather'][0]['description']}")
else:
    print("City not found")
