import requests

def get_single_user(user_id):
    url = f"https://api.example.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        print("User Data:", response.json())
    else:
        print("User not found")

get_single_user(1)

