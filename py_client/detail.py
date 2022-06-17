import requests
import random
endpoint = "http://localhost:8000/api/products/"

data = {
    'title': "This field is done",
    'price': random.randint(0, 10)
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())