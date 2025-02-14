import requests, random

apiURL = "https://api.open-meteo.com/v1/forecast"

cities = [
    {"name": "Tokyo", "lat": 35.6895, "lon": 139.6917},
    {"name": "New York", "lat": 40.7128, "lon": -74.0060},
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Paris", "lat": 48.8566, "lon": 2.3522},
    {"name": "Sydney", "lat": -33.8688, "lon": 151.2093},
    {"name": "Dubai", "lat": 25.276987, "lon": 55.296249},
    {"name": "Moscow", "lat": 55.7558, "lon": 37.6173},
    {"name": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
    {"name": "Rio de Janeiro", "lat": -22.9068, "lon": -43.1729},
]

randomCities = random.sample(cities, 5)

for city in randomCities:
    params = {
        "latitude": city["lat"],
        "longitude": city["lon"],
        "current_weather": "true"
    }

    response = requests.get(apiURL, params=params)

    if response.status_code == 200:
        data = response.json()
        if "current_weather" in data:
            weather = data["current_weather"]
            print(f"{city['name']}: {weather['temperature']}°C")
        else:
            print(f"Weather data not found for {city['name']}.")
    else:
        print("Error occurred: ", response.status_code)
