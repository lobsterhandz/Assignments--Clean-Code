class WeatherDataFetcher:
    def __init__(self):
        # Simulated weather data based on city
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"},
            "Paris": {"temperature": 68, "condition": "Partly Cloudy", "humidity": 55, "city": "Paris"},
            "Berlin": {"temperature": 65, "condition": "Windy", "humidity": 60, "city": "Berlin"},
            "Sydney": {"temperature": 80, "condition": "Sunny", "humidity": 45, "city": "Sydney"},
            "Beijing": {"temperature": 72, "condition": "Smoggy", "humidity": 70, "city": "Beijing"},
            "Moscow": {"temperature": 50, "condition": "Snowy", "humidity": 80, "city": "Moscow"},
            "Mumbai": {"temperature": 88, "condition": "Humid", "humidity": 85, "city": "Mumbai"},
            "São Paulo": {"temperature": 78, "condition": "Rainy", "humidity": 75, "city": "São Paulo"}
        }

    def fetch_weather_data(self, city):
        try:
            print(f"Fetching weather data for {city}...")
            if city not in self.weather_data:
                raise ValueError(f"Weather data for '{city}' is not available.")
            return self.weather_data.get(city, {})
        except ValueError as e:
            print(e)
            return {}
