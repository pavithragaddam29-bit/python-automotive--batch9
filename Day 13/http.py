 #POST Example Using http.client
import http.client
import json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

payload = json.dumps({
    "title": "HTTP Client",
    "body": "Manual HTTP handling",
    "userId": 1
})

headers = {
    "Content-Type": "application/json"
}

conn.request("POST", "/posts", payload, headers)

response = conn.getresponse()
data = response.read()

print("Status:", response.status)
print(data.decode())

conn.close()
