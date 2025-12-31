import requests

base_url = "https://api.example.com/users"

# GET
get_response = requests.get(base_url)
print("GET Status:", get_response.status_code)

# POST
post_data = {"name": "Jhilik", "role": "Trainer"}
post_response = requests.post(base_url, json=post_data)
print("POST Status:", post_response.status_code)

# PUT
put_data = {"name": "Jhilik Barman", "role": "Senior Trainer"}
put_response = requests.put(f"{base_url}/1", json=put_data)
print("PUT Status:", put_response.status_code)

# PATCH
patch_data = {"role": "Lead Trainer"}
patch_response = requests.patch(f"{base_url}/1", json=patch_data)
print("PATCH Status:", patch_response.status_code)

# DELETE
delete_response = requests.delete(f"{base_url}/1")
print("DELETE Status:", delete_response.status_code)

