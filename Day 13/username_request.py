import requests

def get_user_details(username):
    url=f"https://api.github.com/users/{username}"
    response=requests.get(url)

    if response.status_code==200:
        user_data=response.json()
        print("user_name:",user_data["login"])
        print("public reports:",user_data["public_repos"])
    else:
        print("Failed to fetch data")
if __name__=="__main__":
    get_user_details("pavithragaddam29-bit")