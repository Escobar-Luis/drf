import requests


endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={'abc':123}, json={'query': "hello world"}) # API (Application Programming Interface) -> Method HTTP Request
print(get_response.text) # print raw text response
print(get_response.status_code) # print raw text response

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation (JSON) ~ Python Dict
# print(get_response.json())

