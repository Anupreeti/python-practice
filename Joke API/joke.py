import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")
data = response.json()
print(f"{data['setup']}-{data['punchline']}")
