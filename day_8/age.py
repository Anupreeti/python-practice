import requests

def predict_age(name):
    '''
    Function to get the age of a person
    '''
    url = f"https://api.agify.io?name={name}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"Age is : {data['age']}")
        else:
            print(f"Error received: {response.status_code}")
    except requests.RequestException as e:
        print("Error: ", e)
if __name__ == "__main__":
    name = input("Enter name : ")
    predict_age(name)
