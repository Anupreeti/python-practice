import requests

def get_ip():
    url = "https://api64.ipify.org?format=json"
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
    except Exception as e:
        print("Error: ", e)
get_ip()
