import requests
apiUrl = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,
    "page": 1,
    "sparkline": "false"
}

response = requests.get(apiUrl, params=params)
if response.status_code == 200:
    data = response.json()
    for item in data:
        print(f"{item['name']}: ${item['current_price']}")
else:
    print("Failed to fetch data", response.status_code)