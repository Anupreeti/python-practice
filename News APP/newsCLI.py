import argparse
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def latest_news(topic, pages, page_size):
    try:
        for page in range(1,pages+1):
            url = f"https://newsapi.org/v2/everything?q={topic}&page={page}&pageSize={page_size}&from=2025-07-10&to=2025-07-10&sortBy=popularity&apiKey={API_KEY}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if not data['articles']:
                    print("No news on this topic")
                    break
                print(f"-----page {page}-----")
                for i in range(0,page_size):
                    print(f"Title: {data['articles'][i]['title']}")
                    print(f"Date: {data['articles'][i]['publishedAt']}")
                    print(f"Description: {data['articles'][i]['description']}")
            else:
                print("Site gave error please share correct topic")
                break
    except requests.exceptions.RequestException as e:
        print("Error: ", e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get latest news")
    parser.add_argument("--topic", help="Which topic you want news")
    parser.add_argument("--pages", type=int, help="How many pages of news do you want")
    parser.add_argument("--page_size",type=int, help="How many news do you want")
    args= parser.parse_args()

    if args.topic and args.pages and args.page_size:
        latest_news(args.topic, args.pages, args.page_size)
    else:
        print("Please provide the --title, --pages and --page_size")
