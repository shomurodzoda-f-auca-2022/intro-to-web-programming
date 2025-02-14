import requests

apiURL = "https://api.example.com/data?type=latest&limit=5"
response = requests.get(apiURL)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error occurred:",response.status_code)