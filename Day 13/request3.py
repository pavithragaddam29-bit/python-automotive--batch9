import requests

def make_request():
    url = "https://api.github.com"
    headers = {
        "Accept": "application/json",
        "User-Agent": "Python-Web-Client"
    }

    response = requests.get(url, headers=headers)

    print("Request URL:", response.url)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

make_request()
