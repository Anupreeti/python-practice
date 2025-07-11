import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-06-10&sortBy=publishedAt&apiKey={API_KEY}"
try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        if "articles" in data and len(data["articles"]) >= 5:
            for i in range(0,5):
                print(f"Title: {data['articles'][i]['title']} , Source: {data['articles'][i]['source']['name']}")
        else:
            print("Not enough articles found.")
    else:
        print("Issue with the site")
except requests.exceptions.RequestException as e:
    print("Error: ", e)
