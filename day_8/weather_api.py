import requests

def get_weather(city):
    url = f"http://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current_tmp = data['current_condition'][0]['temp_C']
            print(f"Current temperature in {city} is {current_tmp} degree C")
        else:
            print("Failed to get weater data")
    except Exception as e:
        print("Error:, e")

city = input("Enter city name:")
get_weather(city)
