from weather_data_fetcher import WeatherDataFetcher
from data_parser import DataParser

class UserInterface:
    def __init__(self):
        self.weather_fetcher = WeatherDataFetcher()
        self.parser = DataParser()

    def get_detailed_forecast(self, city):
        data = self.weather_fetcher.fetch_weather_data(city)
        return self.parser.parse_weather_data(data)

    def display_weather(self, city):
        data = self.weather_fetcher.fetch_weather_data(city)
        if not data:
            return f"Weather data not available for {city}"
        return self.parser.parse_weather_data(data)

    def run(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if not city.strip():
                print("City name cannot be empty. Please enter a valid city.")
                continue
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no or y/n): ").strip().lower()
            if detailed not in ['yes', 'no', 'y', 'n']:
                print("Invalid input. Please enter 'yes', 'no', 'y', or 'n'.")
                continue
            if detailed in ['yes', 'y']:
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(forecast)