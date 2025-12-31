import requests

response = requests.get("https://api.github.com/invalid-url")

if response.status_code == 200:
    print("Success")
elif response.status_code == 404:
    print("Resource Not Found")
elif response.status_code == 401:
    print("Unauthorized")
else:
    print("Server Error:", response.status_code)
