class DataParser:
    def parse_weather_data(self, data):
        try:
            if not data:
                raise ValueError("Weather data is empty or not available.")
            city = data["city"]
            temperature = data["temperature"]
            condition = data["condition"]
            humidity = data["humidity"]
            return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return f"Missing key in data: {e}"