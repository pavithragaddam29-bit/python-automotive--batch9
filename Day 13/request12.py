import http.client

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

conn.request("GET", "/posts/1")

response = conn.getresponse()

data = response.read()

print("Status:", response.status)
print("Reason:", response.reason)
print("Response Data:")
print(data.decode("utf-8"))

conn.close()

