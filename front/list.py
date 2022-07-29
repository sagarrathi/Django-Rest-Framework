import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
username=input("Username: ")
password = getpass()

token_dict = {
    "username": username,
    "password": password
}
auth_response = requests.post(auth_endpoint, json=token_dict)  # API
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }

    endpoint = "http://127.0.0.1:8000/api/products/"
    get_response = requests.get(endpoint, headers=headers)  # API
    print("json", get_response.json())
