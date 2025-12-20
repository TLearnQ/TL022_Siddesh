import requests
import json

url = "https://reqres.in/api/users/2"
headers = {
    "Authorization": "Bearer reqres-token",
    "Content-Type": "application/json"
}

r = requests.get(url, headers=headers)
data1 = r.json()

with open("file1.json","w") as f:
    json.dump(data1,f,indent=2)


with open("file1.json","r") as f:
    payload = {
    "job": "architect"
}

response = requests.put(url, headers=headers, json=payload)
data = response.json()

with open("file2.json","w") as f:
    json.dump(data,f,indent=2)

if response.status_code == 200 and data["job"] == "architect":
    result = "job updated correctly"
else:
    result = "job not updated"

print("status Code:", response.status_code)
print(data)
print("analysis result:", result)
