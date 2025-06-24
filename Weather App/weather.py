import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

city = input("Enter city: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data.get("main"):
    print(f"Weather in {city}: {data['main']['temp']} degree C")
else:
    print("City not found")
