import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {"userId": 1}

response = requests.get(url, params=params)

print(response.url)
print(response.json()[:2])

 POST with JSON Data
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python Requests",
    "body": "Easy HTTP calls",
    "userId": 5
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print(response.json())

 Headers + Timeout
import requests

url = "https://httpbin.org/get"

headers = {
    "User-Agent": "MyPythonApp",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, timeout=5)

print(response.status_code)
print(response.json())

 Error Handling
import requests

try:
    response = requests.get("https://wrongurl.test", timeout=3)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error:", e)

