import requests

# REST API call (JSON-based)
response = requests.get("https://api.github.com")
print("REST Response:", response.json())

