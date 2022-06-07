import requests


endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={'product_id': "1"}) # API (Application Programming Interface) -> Method HTTP Request
print(get_response.json()) # print raw text response
print(get_response.status_code) # print raw text response

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation (JSON) ~ Python Dict
# print(get_response.json())

