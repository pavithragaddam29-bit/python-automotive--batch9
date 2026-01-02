#Use Case Example: Custom Headers + Manual Control
import http.client

conn = http.client.HTTPSConnection("httpbin.org")

headers = {
    "User-Agent": "CustomClient",
    "Authorization": "Bearer mytoken"
}

conn.request("GET", "/headers", headers=headers)

response = conn.getresponse()
data = response.read()

print("Status:", response.status)
print(data.decode())

conn.close()
