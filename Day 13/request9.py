import requests

url = "https://api.example.com/api/v1/users"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

if response.ok:
    for user in response.json():
        print(user)

