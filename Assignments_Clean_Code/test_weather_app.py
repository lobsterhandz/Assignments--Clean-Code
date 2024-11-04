import unittest
from weather_data_fetcher import WeatherDataFetcher
from data_parser import DataParser
from user_interface import UserInterface

class TestWeatherDataFetcher(unittest.TestCase):
    def setUp(self):
        self.fetcher = WeatherDataFetcher()

    def test_fetch_weather_data_valid_city(self):
        data = self.fetcher.fetch_weather_data("New York")
        self.assertEqual(data["temperature"], 70)
        self.assertEqual(data["condition"], "Sunny")

    def test_fetch_weather_data_invalid_city(self):
        data = self.fetcher.fetch_weather_data("InvalidCity")
        self.assertEqual(data, {})

class TestDataParser(unittest.TestCase):
    def setUp(self):
        self.parser = DataParser()

    def test_parse_weather_data_valid(self):
        data = {"city": "London", "temperature": 60, "condition": "Cloudy", "humidity": 65}
        result = self.parser.parse_weather_data(data)
        self.assertEqual(result, "Weather in London: 60 degrees, Cloudy, Humidity: 65%")

    def test_parse_weather_data_missing_key(self):
        data = {"temperature": 60, "condition": "Cloudy", "humidity": 65}
        result = self.parser.parse_weather_data(data)
        self.assertIn("Missing key in data", result)

    def test_parse_weather_data_empty(self):
        result = self.parser.parse_weather_data({})
        self.assertEqual(result, "Weather data is empty or not available.")

class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.ui = UserInterface()

    def test_get_detailed_forecast_valid_city(self):
        result = self.ui.get_detailed_forecast("Tokyo")
        self.assertEqual(result, "Weather in Tokyo: 75 degrees, Rainy, Humidity: 70%")

    def test_display_weather_invalid_city(self):
        result = self.ui.display_weather("InvalidCity")
        self.assertEqual(result, "Weather data not available for InvalidCity")

if __name__ == "__main__":
    unittest.main()
