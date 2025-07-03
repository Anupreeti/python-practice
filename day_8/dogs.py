import requests

def dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data['message'])
        else:
            print("Failed to get the image url")
    except Exception as e:
        print("Error : ", e)

dog_image()
